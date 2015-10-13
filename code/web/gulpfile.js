var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    jshint = require('gulp-jshint'),
    stylus = require('gulp-stylus'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename');

gulp.task('js', function(){
    gulp.src('js/**/*')
        .pipe(concat('all.js'))
        .pipe(gulp.dest('./public'))
        .pipe(uglify())
        .pipe(gulp.dest('./public'))
        .pipe(rename('all.min.js'));
});

gulp.task('css', function(){
    gulp.src('css/*.styl')
        .pipe(stylus())
        .pipe(concat('all.css'))
        .pipe(gulp.dest('./public'));
});
    

gulp.task('watch', ['js', 'css'], function(){
    gulp.watch('js/*.js')
        .on('change', function(event) {
            console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
            gulp.run('js');
        });
    gulp.watch('css/**/*')
        .on('change', function(event) {
            console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
            gulp.run('css');
        });

});

gulp.task('default', ['watch'], function() {
    // place code for your default task here
    //
});
