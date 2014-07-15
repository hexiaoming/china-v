var gulp = require("gulp");
var less = require("gulp-less");

gulp.task('less', function() {
    return gulp.src(["assets/less/{login,students,shake,shake-rank,promotion}.less"])
        .pipe(less({
            paths: [
                'assets/less',
                'assets/components'
            ]
        }))
        .on('error', console.error)
        .pipe(gulp.dest("assets/css"));
});

gulp.task("watch-less", function() {
    gulp.watch("assets/less/*.less", ["less"]);
});


gulp.task('default', ['less']);