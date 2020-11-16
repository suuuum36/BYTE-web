/* 네비게이터 */

$(".n-1").click(function() {
    $('html, body').animate({
        scrollTop: $(".function-description").offset().top
    },500);
});

$(".n-2").click(function() {
    $('html, body').animate({
        scrollTop: $(".review").offset().top
    },700);
});

$(".n-3").click(function() {
    $('html, body').animate({
        scrollTop: $(".links").offset().top
    },1000);
});

/* 유의사항 팝업 */

$('.notice-button').click(function(){
    $('.notice-board').css("display", "block");
});

$('.cancel-button').click(function(){
    $('.notice-board').css("display", "none");
});

$('.notice-board').click(function(){
    $('.notice-board').css("display", "none");
});

