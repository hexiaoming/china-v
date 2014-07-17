define(function(require) {
    require("jquery");
    require("bootstrap");
    require("velocity");
    require("shake");
    var wechatShare = require('wechat-share');
    var _ = require("underscore");
    var multiline = require("multiline");
    var Backbone = require('backbone/backbone');
    var token = require('js/shake/token');

    wechatShare({
        link: "/shake/",
        desc: '全民摇一摇',
        title: '边看好声音边投票，世界上第一款直播摇一摇投票神器'
    });

    function getVotes() {
        return $.get("/students/vote", {}, "json");
    }

    function vote() {
        return $.post("/students/vote", {
            'audience': token
        }, "json");
    }

    var ENTERING = "entering";
    var VOTING = "voting";
    var status = ENTERING;

    var $container;
    var $votes;
    var $entry;
    var $rules;
    var $rulesOverlay;

    $(function() {
        $container = $(".container");
        $entry = $(".entry");
        $votes = $(".votes");
        $rules = $(".rules");
        $rulesOverlay = $(".rules-overlay");

        $rulesOverlay.click(function() {
            $rules.velocity('fadeOut');
            $rulesOverlay.velocity('fadeOut');
        });
        $rules.on('click', '.exit', function() {
            $rules.velocity('fadeOut');
            $rulesOverlay.velocity('fadeOut');
        });

        $(".button-bar .left").click(function() {
            $rules.velocity('fadeIn');
            $rulesOverlay.velocity('fadeIn');
        });

        $(".button-bar .right").click(function() {
            window.location = "./rank";
        });

        $entry.find("a").click(function(e) {
            e.preventDefault();

            status = VOTING;
            $entry.hide();
            $container.addClass("shake blur");
            $votes.show();
            onVote();
        });
    });

    function onVote() {
        var voting = false;

        var $loaderOverlay = $('<div class="loader-overlay" style="display: none;"></div>');
        $loaderOverlay.appendTo(document.body);

        var LoaderTpl = multiline(function() {
            /*@preserve
        <div class="loader" style="display: none;">
            <img class='preloader' src="/static/img/shake/loading.gif" alt="">
            <div class='selection' style="display: none;">
                <img src="/static/img/shake/vote-head.png"/>
                <ul>
                    <li><a class='btn btn-block' href="#vote">继续投票</a></li>
                    <li><a class='btn btn-block' href="#lottery">进入抽奖</a></li>
                    <li><a class='btn btn-block' href="#rank">查看排名</a></li>
                    <li><a class='btn btn-block' href="#share">马上分享</a></li>
                </ul>
            </div>
        </div>
        */
        }).trim();

        var Loader = Backbone.View.extend({
            initialize: function() {
                this.setElement($(LoaderTpl)[0]);
                this.$selection = this.$el.find(".selection");
                this.$preloader = this.$el.find(".preloader");
            },

            events: {
                'click a[href=#vote]': 'onVote',
                'click a[href=#share]': 'onShare',
                'click a[href=#rank]': 'onRank',
                'click a[href=#lottery]': 'onLottery',
            },

            onRank: function() {
                window.location = "./rank";
            },

            onLottery: function() {
                window.location = "./lottery";
            },

            onShare: function() {

            },

            onVote: function() {
                this.hide();
            },

            show: function() {
                $loaderOverlay.show();
                this.$el.show();
            },

            hide: function() {
                this.$el.hide();
                $loaderOverlay.hide();

                this.$selection.hide();
                this.$preloader.show();
                this.trigger('hide');
            },

            tip: function() {
                this.$selection.show();
                this.$preloader.hide();
            }
        });

        var loader = new Loader();
        loader.on('hide', function() {
            voting = false;
        });

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
                        $tickets.html(data.count);
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
                    $tickets.html(data.count);
                }
            });
        }

        loader.$el.appendTo(document.body);
        $tickets = $votes.find(".tickets");
        refreshVotes();
        window.addEventListener('shake', onShake, false);
    }
});