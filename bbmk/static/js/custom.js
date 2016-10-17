// Custom JS file

// Smooth Scrolling
// Found at https://paulund.co.uk/smooth-scroll-to-internal-links-with-jquery
$(document).ready(function(){
	$('a[href^="#"]').on('click',function (e) {
	    e.preventDefault();

	    var target = this.hash;
	    var $target = $(target);

	    $('html, body').stop().animate({
	        'scrollTop': $target.offset().top
	    }, 900, 'swing', function () {
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

// Fading Navbar
// A personal variation based on:
// http://stackoverflow.com/questions/17713389/how-to-hide-show-nav-bar-when-user-scrolls-up-down
$(document).ready(function() {
	$(window).scroll(function() {
		var scrollTop = $(this).scrollTop();
		if (scrollTop > 0) {
			$('#nav').fadeOut();
		} else {
			$('#nav').fadeIn();
		}
	});
});

// Additional Guest RSVP Functionality
$(document).ready(function() {

	// Guest counter
	var guests = 1

	// Hide-show spans
	$("span#guest_1").hide();
	$("span#guest_2").hide();
	$("span#guest_3").hide();
	$("span#guest_4").hide();
	$("span#guest_5").hide();
	$("span#guest_limit").hide();

	// Add-remove buttons
	$("button#add_guest_button.button-primary").hide();
	$("button#reset_button.button-primary").hide();

	// Show or hide "Add guest" button based on select value
	$("select#guests.u-half-width").change(function() {
		if ($(this).val() == 'Yes') {
			$("button#add_guest_button.button-primary").show();
		} else {
			// struggled with this for a few moments
			guests = 1; 
			$("button#add_guest_button.button-primary").hide();
			$("span#guest_1").hide();
			$("span#guest_2").hide();
			$("span#guest_3").hide();
			$("span#guest_4").hide();
			$("span#guest_5").hide();
			$("span#guest_limit").hide();
		}
	});

	// Add guest
	$("button#add_guest_button.button-primary").click(function() {
		if (guests == 6) {
			$("span#guest_limit").show();
		} else {
			$("span#guest_"+guests).show();
			guests += 1;
		}
	});
});





