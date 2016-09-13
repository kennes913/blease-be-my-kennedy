// Smooth Scrolling
// Found at https://paulund.co.uk/smooth-scroll-to-internal-links-with-jquery
$(document).ready(function(){
	$('a[href^="#"]').on('click',function (e) {
	    e.preventDefault();

	    var target = this.hash;
	    var $target = $(target);

	    $('html, body').stop().animate({
	        'scrollTop': $target.offset().top
	    }, 800, 'swing', function () {
	        window.location.hash = target;
	    });
	});
});

// Sticky Navigation
// Found at http://www.hongkiat.com/blog/css-sticky-position/
$(document).ready(function() {
	var nav = $('#nav').offset().top;
	var stickyNav = function(){
		var scrollTop = $(window).scrollTop();  
		if (scrollTop > nav) { 
    		$('#nav').addClass('sticky');
		} else {
    		$('#nav').removeClass('sticky'); 
		}
	};
	stickyNav();
	$(window).scroll(function() {
  		stickyNav();
	});
});


// Hide Navigation
$(document).ready(function() {
	
});