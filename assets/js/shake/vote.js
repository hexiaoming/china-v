define(function(require) {
    require("jquery");
    require("bootstrap");
    require("shake");
    var _ = require("underscore");
    var multiline = require("multiline");
    var Backbone = require('backbone/backbone');
    var token = require('js/shake/token');

    var voting = false;
    var timestamp = new Date().getTime();
    var $votes;

    var $loaderOverlay = $('<div class="loader-overlay" style="display: none;"></div>');
    $loaderOverlay.appendTo(document.body);

    var LoaderTpl = multiline(function() {
        /*@preserve
        <div class="loader" style="display: none;">
            <img src="/static/img/loading.gif" alt="">
            <p class="alert" style="display: none; margin-bottom: 0px;">操作成功</p>
        </div>
        */
    }).trim();

    var Loader = Backbone.View.extend({
        initialize: function() {
            this.setElement($(LoaderTpl)[0]);
            this.$alert = this.$el.find(".alert");
            this.$img = this.$el.find("img");
        },

        show: function() {
            $loaderOverlay.show();
            this.$el.show();
        },

        hide: function() {
            this.$el.hide();
            $loaderOverlay.hide();
            
            this.$alert.hide();
            this.$img.show();
        },

        tip: function() {
            this.$alert.show();
            this.$img.hide();
        }
    });

    var loader = new Loader();

    function stopRrefreshVotes() {
        timestamp = new Date().getTime();
    }

    function startRefreshVotes() {
        refreshVotes();
    }

    function getVotes() {
        return $.get("/students/vote", {}, "json");
    }

    function vote() {
        return $.post("/students/vote", {
            'audience': token
        }, "json");
    }

    function refreshVotes() {
        setTimeout(function() {
            var _timestamp = new Date().getTime();
            timestamp = _timestamp;
            getVotes().then(function(data) {
                if (data.ret_code === 0 && timestamp === _timestamp) {
                    $votes.html(data.count);
                }
            }).always(function() {
                refreshVotes();
            });
        }, 2000);
    }

    function onShake() {
        if (voting) {
            return console.log("Voting, ignore shake event!");
        }

        var _timestamp = new Date().getTime();
        timestamp = _timestamp;
        loader.show();
        voting = true;
        vote().then(function(data) {
            loader.tip();
            if (data.ret_code === 0 && timestamp === _timestamp) {
                $votes.html(data.count);
            }
        }).always(function() {
            setTimeout(function() {
                loader.hide();
                voting = false;
            }, 1000);
        });
    }

    $(function() {
        loader.$el.appendTo(document.body);
        $votes = $(".votes");
        refreshVotes();
        window.addEventListener('shake', onShake, false);
    });
});