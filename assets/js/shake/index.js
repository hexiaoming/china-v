define(function(require) {
    require("jquery");
    require("bootstrap");
    require("velocity");
    require("shake");
    require("juicer");
    require("components/howler.js/howler.min");
    var id1;
    var id2;
    var option_id;
    var alertify = require("js/alertify");
    var _ = require("underscore");
    var multiline = require("multiline");
    var Backbone = require('backbone/backbone');
    var token = require('js/shake/token');
    var player = new Howl({
        urls: [
            "/static/music/shake_sound_male.ogg",
            "/static/music/shake_sound_male.mp3"
        ],
        onload: function() {},
        volume: 1,
        onloaderror: function() {},
        onplay: function() {}
    });

    var CODE_NO_PLAYING_STUDENT = 2001;
    var VOTE_ID = 6;

    function getVotes() {
        return $.get("/votes/backend/get?vote_id=".concat(VOTE_ID.toString())+"&option_id="+option_id.toString(), {}, "json");
    }

    function vote() {
        return $.post("/votes/backend/post",{
            'vote_id': VOTE_ID,            
            'option_id':option_id
        }, "json");
    }
        
    var ENTERING = "entering";
    var VOTING = "voting";
    var status = ENTERING;
    var voting = false;

    var $container;
    var $votes;
    var $entry;
    var $rules;
    var $rulesOverlay;
    var $shareFlyOverlay;
    $detail= $(".detail");

        function switchToVote(e) {

            status = VOTING;
            $entry.hide();
            $container.addClass("shake blur");
            $votes.show();
            onVote();
        }
   
    function getStudent(){
        return $.post("/votes/backend/pk",{
            'vote_id': VOTE_ID
        }, "json");    
    }
    judge = 0; 
    before = 0;    
    function setTime(){
            t=setTimeout(function() {
                getStudent().then(function(data) {
                    if (data.ret_code === 2) {
                        judge=2;
                        if (judge!==before)
                            makehtml();
                        before = judge;
                    }else if(data.ret_code === 1){
                        judge=1;
                        if (judge!==before) 
                            makehtml();
                        before = judge;  
                    }else{
                        judge=0;
                        if(judge!==before)
                            makehtml2();
                        before = judge;
                    }
                }).always(function(){
                        setTime();
                })
            }, 1000);
        }
    function makehtml2(){
        var tpl = document.getElementById('tpl2').innerHTML;
        $("#entry").text("");
        $("#entry").append(tpl);
        alert("抱歉，现在选手还没有上场。");
    }
    function makehtml(){
        function getStudent(){
            $.ajaxSetup({
                async: false
            });
            return $.post("/votes/backend/pk",{
                'vote_id': VOTE_ID
            }, "json");    
        }
        function setTime(){
            setTimeout(function() {
                getStudent().then(function(data) {
                    if (data.ret_code === 0) {
                        makehtml();
                    }
                }).always(function(){
                    if (data.ret_code !== 0)
                        setTime();
                })
            }, 1000);
        }
        getStudent().then(function(data){
            if (data.ret_code===1999) {
                alert("抱歉，现在选手还没有上场。");
            }else{
                var jsObject = eval(data);
                var tpl = document.getElementById('tpl').innerHTML;
                console.log(jsObject);
                var temp={};
                temp.name1 = jsObject.data[0].name;
                temp.image1 = jsObject.data[0].image;
                (data.ret_code===2)? temp.name2 = jsObject.data[1].name :temp.name2 = jsObject.data[0].name;
                (data.ret_code===2)? temp.image2 = jsObject.data[1].image :temp.image2 = jsObject.data[0].image;
                id1 = jsObject.data[0].id;
                (data.ret_code===2)? id2 = jsObject.data[1].id :id2 = jsObject.data[0].id
                var html = juicer(tpl,temp);
                $("#entry").text("");
                $("#entry").append(html);
                if (data.ret_code === 1){
                    $("#single-vs").hide();
                    $("#single-vote").hide();                
                }
                $detail.find("#choice1").on('touchstart',function(){
                    option_id=id1;
                    switchToVote();
                });
                $detail.find("#choice2").on('touchstart',function(){
                    option_id=id2;
                    switchToVote();
                });
            }
        });
    }
    makehtml();
    setTime();
    $(function() {
        $container = $(".container");
        $entry = $(".entry");
        $votes = $(".votes");
        $rules = $(".rules");
        $rulesOverlay = $(".rules-overlay");
        $shareFlyOverlay = $(".share-fly-overlay");

        $shareFlyOverlay.click(function() {
            $shareFlyOverlay.velocity('fadeOut');
        });

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

//        function switchToVote(e) {

//            status = VOTING;
//            $entry.hide();
//            $container.addClass("shake blur");
//            $votes.show();
//            onVote();
//        }
//        $entry.find("#choice1").click(function(){
//        $("#choice1").click(function(){
//            switchToVote;
//            option_id=id1;
//        });
//        $entry.find("#choice1").on('touchstart', function(){
//        $("#choice1").on('touchstart',function(){
//            switchToVote;
//            option_id=id1
//        });
//        $entry.find("#choice2").click(function(){
//            switchToVote;
//            option_id=id2;
//        });
//        $entry.find("#choice2").on('touchstart', function(){
//            switchToVote;
//            option_id=id2;
//        });
//        $detail.find("#choice1").click(function(){
//            option_id=id1;
//            switchToVote('click');
//        });
//        $detail.find("#choice1").click(option_id=id1);
//        $detail.find("#choice1").click(switchToVote);
//        $detail.find("a").on('touchstart', switchToVote);
//        $detail.find("#choice1").on('touchstart',function(){
//            option_id=id1;
//            switchToVote();
//        });
//        $detail.find("#choice2").on('touchstart',function(){
//            option_id=id2;
//            switchToVote();
//        });

    });

    function onVote() {

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
            console.log
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
                $shareFlyOverlay.velocity('fadeIn');
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
            return $.get("/votes/backend/get?vote_id=".concat(VOTE_ID.toString())+"&option_id="+option_id.toString(), {}, "json");
        }

        function vote() {
            return $.post("/votes/backend/post",{
                'vote_id':VOTE_ID,
                'option_id':option_id
            }, "json");
        }

        function refreshVotes() {
            setTimeout(function() {
                var _timestamp = new Date().getTime();
                timestamp = _timestamp;
                getVotes().then(function(data) {
                    if(timestamp !== _timestamp) {
                        return;
                    }

                    studentPlaying = data.ret_code !== CODE_NO_PLAYING_STUDENT;
                    if (data.ret_code === 0) {
                        $tickets.html(data.count);
                    } else {
                        $tickets.html(0);
                    }
                }).always(function() {
                    refreshVotes();
                });
            }, 1000);
        }

        function onShake() {
            if (voting) {
                return console.log("Voting, ignore shake event!");
            }

            voting = true;

            player.play();
            $(".shakehands").addClass("shakehands-work");
            setTimeout(function() {
                $(".shakehands").removeClass("shakehands-work");

                var _timestamp = new Date().getTime();
                timestamp = _timestamp;

                if (!studentPlaying) {
                    voting = false;
                    alertify.set({
                        delay: 2000
                    });
                    return alertify.log("非常抱歉，学员还没有上场，目前还不能投票。");
                }

                loader.show();
                vote().then(function(data) {
                    if (data.ret_code === 0 && timestamp === _timestamp) {
                        $tickets.html(data.count);
                    }
                    loader.tip();
                }, function() {
                    loader.tip();
                });
            }, 1500);
        }

        loader.$el.appendTo(document.body);
        $tickets = $votes.find(".tickets");
        refreshVotes();
        window.addEventListener('shake', onShake, false);
    }
});
