var gulp = require("gulp");
var less = require("gulp-less");
var uglify = require("gulp-uglify");
var async = require("async");
var rjs = require("requirejs");
var _ = require("underscore");
var gulpif = require('gulp-if');
var sprite = require('css-sprite').stream;
var imagemin = require('gulp-imagemin');
var pngcrush = require('imagemin-pngcrush');
var optipng = require('gulp-optipng');

var options = ['-o2'];


var pkgs = require("./pkg");
pkgs.baseUrl = './assets';

gulp.task('less-shake', function() {
    return gulp.src("assets/less/shake/*.less")
        .pipe(less({
            compress: true,
            paths: [
                'assets/less',
                'assets/components'
            ]
        }))
        .on('error', console.error)
        .pipe(gulp.dest("assets/css/shake"));
});

gulp.task('rjs', function() {
    async.eachSeries(['js/shake/index', 'js/shake/lottery','js/shake/rank'], function(pkg, cb) {
        console.log(pkg);
        rjs.optimize(_.extend(pkgs, {
            name: pkg,
            optimize: "none",
            out: 'assets/' + pkg + ".bundle.js"
        }), function() {
            console.log(pkg, "done!");
            cb();
        }, function(err) {
            console.log(pkg, "error!");
            console.log(err);
            cb(err);
        });
    }, function(err) {
        callback(err);
    });
});

gulp.task('uglify', function() {
    return gulp.src("assets/js/shake/*.bundle.js")
        .pipe(uglify({
            preserveComments: "all"
        }))
        .pipe(gulp.dest("assets/js/shake"));
});


gulp.task('less-base', function() {
    return gulp.src("assets/less/{promotion,students,vote,login}.less")
        .pipe(less({
            paths: [
                'assets/less',
                'assets/components'
            ]
        }))
        .on('error', console.error)
        .pipe(gulp.dest("assets/css"));
});

gulp.task('sprites-shake', function () {
  return gulp.src(['assets/img/shake/shake/*.png'])
    .pipe(sprite({
      name: 'shake.png',
      style: 'sprite.less',
      cssPath: '/static/img/shake/',
      processor: 'less'
    }))
    .pipe(gulpif('*.png', gulp.dest('assets/img/shake/'), gulp.dest('assets/less/shake/')))
});

gulp.task('sprites-lottery', function () {
  return gulp.src(['assets/img/shake/lottery/*.png'])
    .pipe(sprite({
      name: 'lottery.png',
      style: 'sprite1.less',
      cssPath: '/static/img/shake/',
      processor: 'less'
    })) 
    .pipe(gulpif('*.png', gulp.dest('assets/img/shake/'), gulp.dest('assets/less/shake/')))
});
//
//gulp.task('base64', function () {
//  return gulp.src('assets/img/shake/rules-overlay.png')
//    .pipe(sprite({
//      base64: true,
//      style: 'base64.less',
//      processor: 'less'
//    }))
//    .pipe(gulp.dest('assets/less/shake/'));
//});
//
//gulp.task('image',function() {
//    return gulp.src('disc/img/*.png')
//        .pipe(imagemin({
//            progressive:true
//        }))
//        .pipe(gulp.dest('disc/img/test1'));
//});
//
gulp.task('change',function(){
    gulp.src(['assets/img/shake/shake.png','assets/img/shake/lottery.png'])
        .pipe(optipng(options))
        .pipe(gulp.dest('assets/img/shake/'));
});

gulp.task("less", ["less-base", "less-shake"]);

gulp.task("watch-less", function() {
    gulp.watch("assets/less/**/*.less", ["less"]);
});

gulp.task('default', ['less']);
