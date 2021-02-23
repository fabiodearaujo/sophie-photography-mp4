

//Function based on the video from Kevin Powell - https://www.youtube.com/watch?v=SmolT-tV5Lw&t=945s
opacityValue = 0;

$(window).scroll(function() {
    parallax();
})

function parallax() {
    var wScroll = $(window).scrollTop();

    $('.nav-glassify').css('background-color', 'hsla(204, 97%, 64%, '+((wScroll/800)+0.01)+")");

    $('.parallax-bg').css('background-position', 'center '+(wScroll*(-0.2))+'px');

    $('.parallax-line').css('margin-top', (wScroll*0.6)+'px');
    $('.parallax-line').css('opacity', (100-(wScroll/2))+'%');

    $('.parallax-scroll').css('margin-top', (wScroll*0.07)+'px');
    $('.parallax-scroll').css('opacity', (100-(wScroll/2))+'%');

}
