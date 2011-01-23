/*!
 * jQuery JavaScript Library v1.4.4
 * http://jquery.com/
 *
 * Copyright 2010, John Resig
 * Dual licensed under the MIT or GPL Version 2 licenses.
 * http://jquery.org/license
 *
 * Includes Sizzle.js
 * http://sizzlejs.com/
 * Copyright 2010, The Dojo Foundation
 * Released under the MIT, BSD, and GPL Licenses.
 *
 * Date: Thu Nov 11 19:04:53 2010 -0500
 */
(function( window, undefined ) {

    // Use the correct document accordingly with window argument (sandbox)
    var document = window.document;
    var jQuery = (function() {

	    // Define a local copy of jQuery
	    var jQuery = function( selector, context ) {
		// The jQuery object is actually just the init constructor 'enhanced'
		return new jQuery.fn.init( selector, context );
	    },

	    // Map over jQuery in case of overwrite
	    _jQuery = window.jQuery,

	    // Map over the $ in case of overwrite
	    _$ = window.$,

	    // A central reference to the root jQuery(document)
	    rootjQuery,

	    // A simple way to check for HTML strings or ID strings
	    // (both of which we optimize for)
	    quickExpr = /^(?:[^<]*(<[\w\W]+>)[^>]*$|#([\w\-]+)$)/,

	    // Is it a simple selector
	    isSimple = /^.[^:#\[\.,]*$/,

	    // Check if a string has a non-whitespace character in it
	    rnotwhite = /\S/,
	    rwhite = /\s/,

	    // Used for trimming whitespace
	    trimLeft = /^\s+/,
	    trimRight = /\s+$/,

	    // Check for non-word characters
	    rnonword = /\W/,

	    // Check for digits
	    rdigit = /\d/,

	    // Match a standalone tag
	    rsingleTag = /^<(\w+)\s*\/?>(?:<\/\1>)?$/,

	    // JSON RegExp
	    rvalidchars = /^[\],:{}\s]*$/,
	    rvalidescape = /\\(?:["\\\/bfnrt]|u[0-9a-fA-F]{4})/g,
rvalidtokens = /"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g,
		  rvalidbraces = /(?:^|:|,)(?:\s*\[)+/g,

		  // Useragent RegExp
		  rwebkit = /(webkit)[ \/]([\w.]+)/,
		  ropera = /(opera)(?:.*version)?[ \/]([\w.]+)/,
		  rmsie = /(msie) ([\w.]+)/,
		  rmozilla = /(mozilla)(?:.*? rv:([\w.]+))?/,
		  
		  // Keep a UserAgent string for use with jQuery.browser
		  userAgent = navigator.userAgent,

		  // For matching the engine and version of the browser
		  browserMatch,
		  
		  // Has the ready events already been bound?
		  readyBound = false,
		  
		  // The functions to execute on DOM ready
		  readyList = [],

		  // The ready event handler
		  DOMContentLoaded,

		  // Save a reference to some core methods
		  toString = Object.prototype.toString,
		  hasOwn = Object.prototype.hasOwnProperty,
		  push = Array.prototype.push,
		  slice = Array.prototype.slice,
		  trim = String.prototype.trim,
		  indexOf = Array.prototype.indexOf,
		  
		  // [[Class]] -> type pairs
		  class2type = {};

		  jQuery.fn = jQuery.prototype = {
		      init: function( selector, context ) {
			  var match, elem, ret, doc;

			  // Handle $(""), $(null), or $(undefined)
			  if ( !selector ) {
			      return this;
			  }

			  // Handle $(DOMElement)
			  if ( selector.nodeType ) {
			      this.context = this[0] = selector;
			      this.length = 1;
			      return this;
			  }
			  
			  // The body element only exists once, optimize finding it
			  if ( selector === "body" && !context && document.body ) {
			      this.context = document;
			      this[0] = document.body;
			      this.selector = "body";
			      this.length = 1;
			      return this;
			  }

			  // Handle HTML strings
			  if ( typeof selector === "string" ) {
			      // Are we dealing with HTML string or an ID?
			      match = quickExpr.exec( selector );

			      // Verify a match, and that no context was specified for #id
			      if ( match && (match[1] || !context) ) {

				  // HANDLE: $(html) -> $(array)
				  if ( match[1] ) {
				      doc = (context ? context.ownerDocument || context : document);

				      // If a single string is passed in and it's a single tag
				      // just do a createElement and skip the rest
				      ret = rsingleTag.exec( selector );

				      if ( ret ) {
					  if ( jQuery.isPlainObject( context ) ) {
					      selector = [ document.createElement( ret[1] ) ];
					      jQuery.fn.attr.call( selector, context, true );

					  } else {
					      selector = [ doc.createElement( ret[1] ) ];
					  }

				      } else {
					  ret = jQuery.buildFragment( [ match[1] ], [ doc ] );
					  selector = (ret.cacheable ? ret.fragment.cloneNode(true) : ret.fragment).childNodes;
				      }
				      
				      return jQuery.merge( this, selector );
				      
				      // HANDLE: $("#id")
				  } else {
				      elem = document.getElementById( match[2] );

				      // Check parentNode to catch when Blackberry 4.6 returns
				      // nodes that are no longer in the document #6963
				      if ( elem && elem.parentNode ) {
					  // Handle the case where IE and Opera return items
					  // by name instead of ID
					  if ( elem.id !== match[2] ) {
					      return rootjQuery.find( selector );
					  }

					  // Otherwise, we inject the element directly into the jQuery object
					  this.length = 1;
					  this[0] = elem;
				      }

				      this.context = document;
				      this.selector = selector;
				      return this;
				  }

				  // HANDLE: $("TAG")
			      } else if ( !context && !rnonword.test( selector ) ) {
				  this.selector = selector;
				  this.context = document;
				  selector = document.ggs );
			  },
			  
			  ready: function( fn ) {
			      // Attach the listeners
			      jQuery.bindReady();

			      // If the DOM is already ready
			      if ( jQuery.isReady ) {
				  // Execute the function String.call(obj) ] || "object";
			      },

			      isPlainObject: function( obj ) {
				  // Must be an Object; i++ y ) : undefined;
			      },

			      now: function() {
				  return (new Date()).getTime();
			      },

			      // Use of jQuery.browser is frowned upon.
			      // More details .text instead)
			      if ( window[ id ] ) {
				  jQuery.support.scriptEval = true;
				  delete wiif ( !jQuery.acceptData( elem ) ) {
				      return;
				  }

				  elem = elem == window ?
				  [1] = parts[1] ? "." + parts[1] : "";

				  if ( value === undefined ) {
				      s, " ").indexOf( className ) > -1 ) {
				  retu handleObjIn, handleObj;

				  if ( handler.handler ) {
				      handleObjIn = handler;
				      handler = handleObjIn.handler;
				  }

				  // May ];

				  if ( !elemData || !events ) {
				      return;
				  }
			      };

			      if ( (!special._default || special._default.call( elem, event ) r ),
				   jQuery.ext up the tree
				   while ( parent && parent !== this ) {
				       parent = parent.p ( var i = 0, l = this.length; i(function(){

						   var chunker = /((?:\((?:\([^()]+\)|[^()]+)+\)|\[(?:\[[^\[\]]*\]|['"][^'"]*['"]|[^\[\]'"]+)+\]|\\.|[^ >zle( expr, null, null, set );
};

Sizzle.matchesSelector = function( node, expr ) {
return Sizzle( expr, null, null, [node] ).length > 0;
};

Sizzle.find = function( expr, context, isXML ) {
var set;

if ( !expr ) {
return [];
}

for ( var i = 0, l = Expr.order.length; i < l; i++ ) {
var match,
type = Expr.order[i];

if ( (match = Expr.leftMatch[ type ].exec( expr )) ) {
var left = match[1];
match.splice( 1, 1 )s attributes, doesn't catch changes (in 3.2)
																   div.lastChild.className = "e";

																   if ( div.getElementsByClassName("e").length === 1 ) {
																       return;
																   }
																   
																   Expr.order.splice(1, 0, "CLASS");
																   Expr.find.CLASS = function( match, context, isXML ) {
																       if ( typeof context.getElementsByClassName !== "undefined" && !isXML ) {
																	   return context.getElementsByClassName(match[1]);
																       }
																   };

																   // release memory in IE
																   div = null;
																   })();

								    function dirNodeCheck( dir, cur, doneName, checkSet, nodeCheck, isXML ) {
									for ( var i = 0, l = checkSet.length; i < l; i++ ) {
									    var elem = checkSet"alpha(opacity=" + value * 100 + ")",
										filter = style.filter || "";

									    style.filter = ralpha.test(filter) ?
										filter.replace(ralpha, opacity) :
										style.filter + ' ' + opacity;
									}
								    };
								    }

								   if ( document.defaultView && document.defaultView.getComputedStyle ) {
								       getComputedStyle = function( elem, newName, name ) {
									   var ret, defaultView, computedStyle;

									   name = name.replace( rupper, "-$1" ).toLowerCase();

									   if ( !(defaultView = elem.ownerDocument.defaultView) ) {
									       return undefined;
									   }

									   if ( (computedStyle = defaultView.getComputedStyle( elem, null )) ) {
									       ret = computedStyle.getPropertyValue(;

														    jQuery.each( [ "", "X", "Y" ], function (index, value) {
															    elem.style[ "overflow" + value ] = options.overflow[index];
															} );