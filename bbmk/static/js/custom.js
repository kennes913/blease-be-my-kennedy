// Ad hoc functionality
// By: Sean Kennedy

/* Fading Navbar:
	Code found here:
	http://stackoverflow.com/questions/17713389/how-to-hide-show-nav-bar-when-user-scrolls-up-down
*/

$(document).ready(function() {
	var width = $(window).width();
	if (width > 450) {
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


// RSVP Form Add Guest Functionality

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
 Navigation dropdown mobile device menu:
 	HTML/CSS can be found at https://codepen.io/RRoberts/pen/OXxkzm
*/

$(document).ready(function() {
	$(".mobile-two .menu-toggle").click(function() {
		$(this).parent().next(".mobile-nav").toggle(0 , "display");
	});
});


// Remove photos based on media query size (This can be done with css instead!)

$(document).ready(function(){
	var reception_photo = $("div.six:nth-child(2) > img:nth-child(1)")
	var ceremony_photo = $(".four > img:nth-child(1)")
	var width = $(window).width();
	if (width < 600){
		reception_photo.hide();
		ceremony_photo.hide();
	} else {
		reception_photo.show();
		ceremony_photo.show();
	};

});


//Remove homepage background image. 

$(document).ready(function(){
	var welcome  = $("#welcome");
	var announce  = $(".home_header > h1:nth-child(1)");
	var footer  = $("footer");
	var width = $(window).width();
	if (width < 1025){
		welcome.css("background-image", "none");
		announce.css("color", "#000000");
		footer.hide();
		width > 400 ? announce.css("padding-left", "100px") : announce.css("padding-left", "0px");
	} else {
		welcome.css("background-image", "url('/static/images/home_photo.png')");
		footer.show();
	};
});


// Shrink home header

$(document).ready(function(){
	var announce  = $(".home_header > h1:nth-child(1)");
	var width = $(window).width();
	if (width < 400){
		announce.css("font-size", '4em');
	};
});


// Resize RSVP Form Fields based on devie

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









