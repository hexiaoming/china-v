var gulp = require("gulp");
var less = require("gulp-less");

gulp.task('less-shake', function() {
    return gulp.src("assets/less/shake/*.less")
        .pipe(less({
            paths: [
                'assets/less',
                'assets/components'
            ]
        }))
        .on('error', console.error)
        .pipe(gulp.dest("assets/css/shake"));
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