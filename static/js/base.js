

//Function based on the video from Kevin Powell - https://www.youtube.com/watch?v=SmolT-tV5Lw&t=945s

$(window).scroll(function() {
    parallax();
})

function parallax() {
    var wScroll = $(window).scrollTop();

    $('.nav-glassify').css('opacity', ((wScroll/4)+60)+'%');

    $('.parallax-bg').css('background-position', 'center '+(wScroll*(-0.2))+'px');

    $('.parallax-line').css('margin-top', (wScroll*0.6)+'px');
    $('.parallax-line').css('opacity', (100-(wScroll/2))+'%');

}