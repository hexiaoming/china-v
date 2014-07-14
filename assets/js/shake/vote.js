define(function(require) {
    require("jquery");
    require("bootstrap");
    require("shake");
    var multiline = require("multiline");


    var refreshing = true;
    var refreshTask = -1;

    function stopRrefreshVotes() {
        refreshing = false;
        clearTimeout(refreshTask);
    }

    function startRefreshVotes() {
        refreshing = true;
        refreshVotes();
    }

    function getVotes() {
        $.get("/students/vote", {}, "json");
    }


    function vote() {
        $.post("/students/vote", {}, "json");
    }

    function refreshVotes() {
        var $votes = $(".votes");
        refreshTask = setTimeout(function() {
            if (!refreshing) {
                return;
            }
            getVotes().then(function(data) {
                if (data.ret_code === 0) {
                    votes.html(data.count);
                }
            }).always(function() {
                refreshVotes();
            });
        }, 1000);
    }

    $(refreshVotes);

    $(function() {
        window.addEventListener('shake', function() {
            stopRrefreshVotes();
        }, false);
    });
});