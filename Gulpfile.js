var gulp = require("gulp");
var less = require("gulp-less");
var uglify = require("gulp-uglify");
var async = require("async");
var rjs = require("requirejs");
var _ = require("underscore");

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
    async.eachSeries(['js/shake/index', 'js/shake/lottery'], function(pkg, cb) {
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

gulp.task("less", ["less-base", "less-shake"]);

gulp.task("watch-less", function() {
    gulp.watch("assets/less/**/*.less", ["less"]);
});

gulp.task('default', ['less']);