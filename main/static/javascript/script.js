
$(document).ready(function() {
  $('.carousel').carousel({'duration': 50});
  $('#home').mousedown(function(e) {
    console.log('clickflippyfuck')
    $('.flipper-left').addClass('box-rotated');
    // $('#bottom-left-flipper').addClass('box-rotated');
    e.preventDefault();
    e.stopPropagation();
  })
  $('#home').mouseup(function(e) {
    console.log('clickflippyfuck')
    $('.flipper-left').removeClass('box-rotated')
    e.preventDefault();
    e.stopPropagation();
  })
  $('#location').mousedown(function(e) {
    console.log('clickflippyfuck')
    $('.flipper-left').addClass('box-rotated');
    $('.flipper-image').addClass('box-rotate');
    e.preventDefault();
    e.stopPropagation();
  })
  $('#location').mouseup(function(e) {
    console.log('clickflippyfuck')
    $('.flipper-left').removeClass('box-rotated')
    $('.flipper-image').removeClass('box-rotate')
    e.preventDefault();
    e.stopPropagation();
  })
  $('#past').mousedown(function(e) {
    console.log('clickflippyfuck')
    $('.flipper-image').addClass('box-rotate');
    e.preventDefault();
    e.stopPropagation();
  })
  $('#past').mouseup(function(e) {
    console.log('clickflippyfuck')
    $('.flipper-image').removeClass('box-rotate')
    e.preventDefault();
    e.stopPropagation();
  })
  $('#form21, #form22, #form23').bind('keyup', function() {
    console.log('yaoaooaoaoaoao')
    if(allFilled()) $('#problematic').removeAttr('disabled');
  });
})


function allFilled() {
  var filled = true;
  $('.req').each(function() {
      if($(this).val() == '') filled = false;
  });
  return filled;
}

// allFilled();

function changeDiv() {
  $('#small-mid').addClass('important')
  $('#big-mid').addClass('important')
  $('#main').css('display', 'block')
  $('#gallery').css('display', 'none')
  $('#home').removeClass('pink');
  $('#location').addClass('pink');
  $('#past').removeClass('pink');
}

function changeBack() {
  $('#small-mid').removeClass('important')
  $('#big-mid').removeClass('important')
  $('#main').css('display', 'none')
  $('#gallery').css('display', 'none')
  $('#home').addClass('pink');
  $('#location').removeClass('pink');
  $('#past').removeClass('pink');
}

function displayGallery() {
  $('#small-mid').addClass('important')
  $('#big-mid').addClass('important')
  $('#gallery').css('display', 'block');
  $('#main').css('display', 'none');
  $('#past').addClass('pink');
  $('#home').removeClass('pink');
  $('#location').removeClass('pink');
}

function closeModal() {
  console.log('close that shit modal for sure')
  $('#modalContactForm').modal('hide');
}

function footerShit() {
  var myHeight = document.getElementById('center').clientHeight;
  console.log(myHeight);
  console.log($(window).height() * .66)
  if (myHeight > $(window).height() * .66) {
    console.log(myHeight);
  }
}

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
