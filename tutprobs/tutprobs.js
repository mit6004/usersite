// cjt, September 2003
// appears to work with IE6, Mozilla 1.4, Firebird 0.6.1, Safari 1.0, Netscape 7.1

// toggle visibility of specified answer
function toggle(el) {
    whichEl = document.getElementById("answer"+el);
    whichIm = document.images["ctl"+el];
    if (whichEl.style.display == "none") {
      whichEl.style.display = "block";
      whichIm.src = "hide.gif";		
    } else {
      whichEl.style.display = "none";
      whichIm.src = "show.gif";
    }
}

// should be called after the document has been loaded
function hideall() {
    tempColl = document.getElementsByTagName("DIV");
    for (i=0; i<tempColl.length; i++) {
      if (tempColl.item(i).className == "answer")
        tempColl.item(i).style.display = "none";
    }
    tempColl = document.images;
    for (i=0; i<tempColl.length; i++) {
      if (tempColl.item(i).className == "hideshow")
        tempColl.item(i).src = "show.gif";
    }
}

function showall() {
    tempColl = document.getElementsByTagName("DIV");
    for (i=0; i<tempColl.length; i++) {
      if (tempColl.item(i).className == "answer")
        tempColl.item(i).style.display = "block";
    }
    tempColl = document.images;
    for (i=0; i<tempColl.length; i++) {
      if (tempColl.item(i).className == "hideshow")
        tempColl.item(i).src = "hide.gif";
    }
}

// load images we'll need
if (document.images) {
  hide = new Image();
  hide.src = "hide.gif";
}
