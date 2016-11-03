// Ad hoc functionality
// By: Sean Kennedy


/* Fading Navbar:
	Code found here:
	http://stackoverflow.com/questions/17713389/how-to-hide-show-nav-bar-when-user-scrolls-up-down
*/

$(document).ready(function() {
	var width = $(window).width();
	if (width > 785) {
		$(window).scroll(function() {
			var scrollTop = $(this).scrollTop();
			if (scrollTop > 0) {
				$('#nav').fadeOut();
				$('#home-nav').fadeOut();
			} else {
				$('#nav').fadeIn();
				$('#home-nav').fadeIn();
			}
		});
	}; 
});


/* 
 Navigation dropdown mobile device menu:
 	HTML/CSS can be found at https://codepen.io/RRoberts/pen/OXxkzm
*/

$(document).ready(function() {
	$(".mobile-two .menu-toggle").click(function() {
		$(this).parent().next(".mobile-nav").toggle(0 , "display");
	});
});


/*
 RSVP Form Add Guest Functionality
*/

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

/* 
 Resize RSVP Form Fields based on device
*/


$(document).ready(function(){
	var form_name = $('#name')
	var form_email = $('#email')
	var form_events = $('#events')
	var form_guests = $('#guests')
	var width = $(window).width();
	if (width < 400){
		form_name.css('width', '100%');
		form_email.css('width', '100%');
		form_events.css('width', '100%');
		form_guests.css('width', '100%');
	};
});









