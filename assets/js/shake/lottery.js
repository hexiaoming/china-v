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
        desc: '中国好声音',
        title: '全民摇一摇'
    });

    var $container;
    var $rules;
    var $rulesOverlay;
    var $form;
    var form;
    var phone;
    var canvas;
    var $canvas;
    var ctx;

    function initCanvas() {
        canvas = document.querySelector('canvas');
        $canvas = $(canvas);
        ctx = canvas.getContext('2d');
        var w = canvas.width,
            h = canvas.height;

        ctx.fillStyle = 'transparent';
        ctx.fillRect(0, 0, w, h);
        ctx.fillStyle = '#DF0422';
        ctx.fillRect(0, 0, w, h);
    }

    function lauchCanvas() {
        var down = false;

        var w = canvas.width,
            h = canvas.height;

        function eventDown(e) {
            down = true;
        }

        function eventUp(e) {
            down = false;
        }

        function eventMove(e) {
            e.preventDefault();
            if (down) {
                var offset = $(canvas).offset();
                if (e.changedTouches) {
                    e = e.changedTouches[e.changedTouches.length - 1];
                }
                console.log('page x, y:', e.pageX, e.pageY);
                var x = e.pageX - offset.left,
                    y = e.pageY - offset.top;
                console.log('pos', x, y);
                with(ctx) {
                    beginPath()
                    arc(x, y, 10, 0, Math.PI * 2);
                    fill();
                }
            }
        }

        ctx.globalCompositeOperation = 'destination-out';
        document.body.addEventListener('touchmove', eventMove, false);
        document.body.addEventListener('mousemove', eventMove, false);
        document.body.addEventListener('touchstart', eventDown, false);
        document.body.addEventListener('touchend', eventUp, false);
        document.body.addEventListener('mousedown', eventDown, false);
        document.body.addEventListener('mouseup', eventUp, false);
    }

    $(function() {
        initCanvas();
        $form = $(".phone-prompt-form");
        form = $form[0];
        $container = $(".container");
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

        $(".button-bar .right").click(function() {});

        $form.submit(function(e) {
            e.preventDefault();
            if (form.phone.value === '') {
                return;
            }

            phone = form.phone.value;
            $form.parent().velocity('fadeOut');
            $canvas.addClass("first");
            lauchCanvas();
        });
    });
});