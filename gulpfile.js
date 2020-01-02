let gulp = require('gulp');
let cleanCSS = require('gulp-clean-css');
let uglify = require('gulp-uglify');
 
gulp.task('minify-css', function() {
  return gulp.src('./layouts/src/css/all.css')
    .pipe(cleanCSS({compatibility: 'ie8'}))
    .pipe(gulp.dest('./layouts/src/css/min.css/'));
});

gulp.task('min-js', function() {
  return gulp.src('./layouts/src/js/openMenu.js')
    .pipe(uglify())
    .pipe(gulp.dest('./layouts/src/js/min.js/openMenu.min.js'));
});