
```
undefined fenced block code
```

``` javascript
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```

```json
{
  "run_rspec_command": "source ~/.rvm",
  "run_single_rspec_command": "source"
}
``` 

~~~js
// Cross-browser xml parsing
var parseXML = function( data ) {
  var xml, tmp;
  if ( !data || typeof data !== "string" ) {
    return null;
  }
  try {
    if ( window.DOMParser ) { // Standard
      tmp = new DOMParser();
      xml = tmp.parseFromString( data , "text/xml" );
    } else { // IE
      xml = new ActiveXObject( "Microsoft.XMLDOM" );
      xml.async = false;
      xml.loadXML( data );
    }
  } catch( e ) {
    xml = undefined;
  }
  if ( !xml || !xml.documentElement || xml.getElementsByTagName( "parsererror" ).length ) {
    jQuery.error( "Invalid XML: " + data );
  }
  return xml;
};

// Bind a function to a context, optionally partially applying any arguments.
var proxy = function( fn, context ) {
  var tmp, args, proxy;

  if ( typeof context === "string" ) {
    tmp = fn[ context ];
    context = fn;
    fn = tmp;
  }

  // quick check to determine if target is callable, in the spec
  // this throws a typeerror, but we will just return undefined.
  if ( !jquery.isfunction( fn ) ) {
    return undefined;
  }

  // simulated bind
  args = core_slice.call( arguments, 2 );
  proxy = function() {
    return fn.apply( context || this, args.concat( core_slice.call( arguments ) ) );
  };

  // set the guid of unique handler to the same of original handler, so it can be removed
  proxy.guid = fn.guid = fn.guid || jquery.guid++;

  return proxy;
};

sound.play = function() {}
sound.prototype = { something; }
sound.prototype.play = function() {}
sound.prototype.play = myfunc
var parser = document.createelement('a');
parser.href = "http://example.com:3000/pathname/?search=test#hash";
parser.hostname; // => "example.com"
~~~

```ruby
class htmlprocessor

  # called before parsing anything
  def start_parsing(scope_name)
    @line = ""
    @offset = 0
    @text= []
  end

  # called after parsing everything
  def end_parsing(scope_name)
    @text.each_with_index do |line, index|
      @text[index] = "<span class='l l-#{index+1} #{scope_name.gsub('.',' ')}'>#{line}</span>"
    end
    puts @text.join("")
  end

  # called before processing a line
  def new_line(line_content)
    @offset = 0
    @line = line_content.clone
    @text << @line
  end

  def open_tag(tag_name, position_in_current_line)
    tag = "<s class='#{tag_name.gsub("."," ")}'>"
    @line.insert(position_in_current_line + @offset, tag)
    @offset += tag.size
  end

  def close_tag(tag_name, position_in_current_line)
    tag = "</s>"
    @line.insert(position_in_current_line + @offset, tag)
    @offset += tag.size
  end

end

syntax = textpow.syntax('ruby') # or 'source.ruby' or 'lib/textpow/syntax/source.ruby.syntax'
processor = htmlprocessor.new
syntax.parse(text, processor)

require file.expand_path('../boot', __file__)

require 'rails/all'

if defined?(bundler)
  # if you precompile assets before deploying to production, use this line
  bundler.require(*rails.groups(:assets => %w(development test)))
  # if you want your assets lazily compiled in production, use this line
  # bundler.require(:default, :assets, rails.env)
end

require 'rubygems'

# set up gems listed in the gemfile.
env['bundle_gemfile'] ||= file.expand_path('../../gemfile', __file__)

require 'bundler/setup' if file.exists?(env['bundle_gemfile'])
```

~~~py
import sublime
import sublime_plugin

import os
import fnmatch
import re

# on plugin_load read settings
# on plugin_load create notes directory if it does not exists

class noteslistcommand(sublime_plugin.applicationcommand):
    def __init__(self):
        self.notes_dir = os.path.expanduser("~/dropbox/notes/")

    def find_notes(self, file):
        if fnmatch.fnmatch(file, '*.note'):
            return re.sub('\.note$', '', file)

    def open_note(self, index):
        if index == -1:
            return
        file = os.path.join(self.notes_dir, self.file_list[index] + ".note")
        # self.window.run_command("new_pane",{"move": true})
        view = sublime.active_window().open_file(file)

    def run(self):
        window = sublime.active_window()
        self.file_list = [self.find_notes(file) for file in os.listdir(self.notes_dir)]
        window.show_quick_panel(self.file_list, self.open_note)

~~~

``` coffee
application.directive "scopebar", [], ->
  replace: true
  templateurl: 'partials/scope_bar'

  link: (scope, element, attr) ->
    preview = element.prev()
    preview.bind "mouseover", (event) ->
      active = {}
      active.scope = event.target.dataset.entityscope

      if active.scope
        active_scope_rule = getscopesettings(active.scope)
        active.name = active_scope_rule.name if active_scope_rule

      scope.$apply ->
        # highlight in sidebar
        scope.$parent.hovered_rule = active_scope_rule

    preview.bind "mouseout", (event) ->
      # unhighlight in sidebar
      scope.$parent.hovered_rule = null

    preview.bind "dblclick", (event) ->
      active = {}
      active.scope = event.target.dataset.entityscope

      if active.scope
        active_scope_rule = getscopesettings(active.scope)
        showpopover active_scope_rule, event



    showpopover = (rule, event) ->
      scope.$apply ->
        scope.$parent.new_popover_visible = false
        scope.$parent.popover_rule = rule
        scope.$parent.edit_popover_visible = true

      popover = $("#edit-popover")

      if popover.is('.slide')
        left_offset = $("#gallery").width()
      else
        left_offset = 0

      offset =
        left: (popover.width() / 2) + 10 + left_offset
        top: 24

      popover.css({
        "left": event.pagex - offset.left
        "top": event.pagey + offset.top
      }).addclass("on-bottom")


    getscopesettings = (active_scope) ->
      return unless scope.$parent.jsontheme.settings

      return scope.$parent.jsontheme.settings.find (item) ->
        return unless item.scope

        item_scopes = item.scope.split(', ')

        match = item_scopes.filter (item_scope) ->
          item_scopes_arr = item_scope.split('.')
          active_scope_arr = active_scope.split('.')

          return (item_scopes_arr.subtract active_scope_arr).length < 1

        return item if match.length

```  

```scala
package akka

import akka.actor.ActorSystem
import akka.actor.ExtendedActorSystem
import akka.actor.Actor
import akka.actor.Terminated
import akka.actor.ActorLogging
import akka.actor.Props
import akka.actor.ActorRef
import scala.util.control.NonFatal

/**
 * Main class to start an [[akka.actor.ActorSystem]] with one
 * top level application supervisor actor. It will shutdown
 * the actor system when the top level actor is terminated.
 */
object Main {

  /**
   * @params args one argument: the class of the application supervisor actor
   */
  def main(args: Array[String]): Unit = {
    if (args.length != 1) {
      println("you need to provide exactly one argument: the class of the application supervisor actor")
    } else {
      val system = ActorSystem("Main")
      try {
        val appClass = system.asInstanceOf[ExtendedActorSystem].dynamicAccess.getClassFor[Actor](args(0)).get
        val app = system.actorOf(Props(appClass), "app")
        val terminator = system.actorOf(Props(classOf[Terminator], app), "app-terminator")
      } catch {
        case NonFatal(e) ⇒ system.shutdown(); throw e
      }
    }
  }

  class Terminator(app: ActorRef) extends Actor with ActorLogging {
    context watch app
    def receive = {
      case Terminated(_) ⇒
        log.info("application supervisor has terminated, shutting down")
        context.system.shutdown()
    }
  }

}
```

``` sass    
@mixin border-radius($radius) {
  -webkit-border-radius: $radius;
     -moz-border-radius: $radius;
      -ms-border-radius: $radius;
       -o-border-radius: $radius;
          border-radius: $radius;
}

.box { @include border-radius(10px); }
```  

``` scss
@mixin border-radius($radius) {
  -webkit-border-radius: $radius;
     -moz-border-radius: $radius;
      -ms-border-radius: $radius;
       -o-border-radius: $radius;
          border-radius: $radius;
}

.box { @include border-radius(10px); }
```  

```  bash
function git_remote {
  about 'adds remote $GIT_HOSTING:$1 to current repo'
  group 'git'

  echo "Running: git remote add origin ${GIT_HOSTING}:$1.git"
  git remote add origin $GIT_HOSTING:$1.git
}

function git_first_push {
  about 'push into origin refs/heads/master'
  group 'git'

  echo "Running: git push origin master:refs/heads/master"
  git push origin master:refs/heads/master
}

function git_pub() {
  about 'publishes current branch to remote origin'
  group 'git'
  BRANCH=$(git rev-parse --abbrev-ref HEAD)

  echo "Publishing ${BRANCH} to remote origin"
  git push -u origin $BRANCH
}
```  

``` java
import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class ReadAndPrintScores
{
    public static void main(String[] args)
    {   try
    {   Scanner s = new Scanner( new File("scores.dat") );
        while( s.hasNextInt() )
        {   System.out.println( s.nextInt() );
        }
    }
    catch(IOException e)
    {   System.out.println( e );
    }
    }
}
``` 

```  less
@base: #f938ab;
.box-shadow(@style, @c) when (iscolor(@c)) {
  -webkit-box-shadow: @style @c;
  -moz-box-shadow:    @style @c;
  box-shadow:         @style @c;
}
.box-shadow(@style, @alpha: 50%) when (isnumber(@alpha)) {
  .box-shadow(@style, rgba(0, 0, 0, @alpha));
}
.box {
  color: saturate(@base, 5%);
  border-color: lighten(@base, 30%);
  div { .box-shadow(0 0 5px, 30%) }
}
```  

```  css
h2 {
    font-size: 1.5em;
    background-color: #ccc;
    margin: 20px;
    padding: 40px;
}
```  

```  php
<?php
class Programmer {
        // Class Properties
        var $name;         // Programmer's name
        var $experience;   // How long has been programming
        var $lang;         // Favorite Language
        var $education;    // Highest degree earned
        // Class Constructor - function same name as the class
        function Programmer($name, $experience, $lang, $education) {
             $this->name=$name;
             $this->experience=$experience;
             $this->lang=$lang;
             $this->education=$education;
        }
        // Getter/Setter functions for all properties in the class
        function get_name() {
             return $this->name;
        }
        function set_name($newname) {
             $this->name = $newname;
        }
        function get_experience() {
             return $this->experience;
        }
        function set_experience($newexperience) {
             $this->experience = $newexperience;
        }
        function get_lang() {
             return $this->lang;
        }
        function set_lang($newlang) {
             $this->lang = $newlang;
        }
        function get_education() {
             return $this->education;
        }
        function set_education($neweducation) {
             $this->education = $neweducation;
        }
        // Utility data dump function
        function output() {
             echo "Programmer Name: ".$this->name."<br>";
             echo $this->name." has ".$this->experience." years of programming experience.<br>";
             echo $this->lang." is ".$this->name."'s favorite programming language.<br>";
             echo $this->name." holds the degree: ".$this->education."<br><br>";
        }
   }
   // Instantiating a programmer
   $paul = new Programmer('Paul Conrad',12,'C++','Bachelor of Science in Computer Science');
   $paul->output();
   // Oops, Paul has programmed alot longer than 12 year, really is 22 years
   $paul->set_experience(22);
   $paul->output();
?>
```  

```  xml
<dict>
  <key>name</key>
  <string>comment</string>
  <key>scope</key>
  <string>markup.raw.block.fenced comment, markup.raw.block.fenced comment punctuation</string>
  <key>settings</key>
  <dict>
    <key>foreground</key>
    <string>#999999</string>
  </dict>
</dict>
<dict>
```  

```  html
<!DOCTYPE html>
<html>
<body>
<p>
    My Bonnie lies over the ocean.
    My Bonnie lies over the sea.
    My Bonnie lies over the ocean.
    Oh, bring back my Bonnie to me.
</p>
<p>Note that your browser ignores the layout!</p>
</body>
</html>
```  


```  sql
-- cr_spatial_index.sql
--
-- Note: if geometries do not span more than 1 row, you can remove
-- the DISTINCT qualifier from the SELECT statement
--
declare
   cursor c1 is SELECT DISTICT sdogid from POLYGON_SDOGEOM;
   gid number;
   i number; 
begin
     i := 0;
     for r in c1 loop
       begin
        gid:= r.sdo_gid;
        sdo_admin.update_index_fixed('POLYGON', gid, 15, FALSE, FALSE, FALSE);
        exeption when others then
          dbms_output.put_line('error for gid'||to_char(gid)||':  '||SQLERRM );
       end;
       i:=  i + 1;
       if i = 50 then
          commit;
          i:= 0;
       end if;
     endloop;
commit;
end;
/
```

```  yaml
--- !clarkevans.com/^invoice
invoice: 34843
date   : 2001-01-23
bill-to: &id001
    given  : Chris
    family : Dumars
    address:
        lines: |
            458 Walkman Dr.
            Suite #292
        city    : Royal Oak
        state   : MI
        postal  : 48046
ship-to: *id001
product:
    - sku         : BL394D
      quantity    : 4
      description : Basketball
      price       : 450.00
    - sku         : BL4438H
      quantity    : 1
      description : Super Hoop
      price       : 2392.00
tax  : 251.42
total: 4443.52
comments: >
    Late afternoon is best.
    Backup contact is Nancy
    Billsmer @ 338-4338.
total: 4443.52
```

``` c
#include <stdio.h>
 
int main()
{
   int n, reverse = 0;
 
   printf("Enter a number to reverse\n");
   scanf("%d",&n);
 
   while (n != 0)
   {
      reverse = reverse * 10;
      reverse = reverse + n%10;
      n = n/10;
   }
 
   printf("Reverse of entered number is = %d\n", reverse);
 
   return 0;
}
```

``` cpp
//An example of using templated class to create stack depends on underlying array.
#include<iostream>
#include<cstdlib>
#define default_value 10
using namespace std;
 
template< class T > class Stack
{
    public:
    Stack(int = default_value);//default constructor
    ~Stack()//destructor
    {delete [] values;}
    bool push( T );
    T pop();
    bool isEmpty();
    bool isFull();
    private:
    int size;
    T *values;
    int index;
 
};
 
template< class T > Stack<T>::Stack(int x):
    size(x),//ctor
    values(new T[size]),
    index(-1)
{ /*empty*/  }
 
template< class T > bool Stack<T>::isFull()
{
    if((index + 1) == size )
    return 1;
    else
    return 0;
}
 
template< class T > bool Stack<T>::push(T x)
{
    bool b = 0;
    if(!Stack<T>::isFull())
    {
    index += 1;
    values[index] = x;
    b = 1;
    }
    return b;
}
```

``` c++
template< class T > bool Stack<T>::push(T x)
{
    bool b = 0;
    if(!Stack<T>::isFull())
    {
    index += 1;
    values[index] = x;
    b = 1;
    }
    return b;
}
```


```  erlang
-module(bowling).
-export([test/0,score/1]).
-import(lists,[duplicate/2]).

 test() ->
 0 = score(duplicate(10,{0,0})),
 60 = score(duplicate(10,{3,3})),
 21 = score([{4,6},{3,5}|duplicate(8,{0,0})]),
 23 = score([{4,6},{5,3}|duplicate(8,{0,0})]),
 26 = score([{10,pass},{5,3}|duplicate(8,{0,0})]),
 15 = score(duplicate(9,{0,0}) ++ [{4,6},{5,nothrow}]),
 18 = score(duplicate(9,{0,0}) ++ [{10,pass},{5,3}]),
 ok.

 score(Frame) ->
   score(Frame,1,0).

 score([{10,_}|T], 10, Total) ->
   Total + 10 + element(1,hd(T)) + element(2,hd(T));
 score([{First,Second}|T], Turn, Total) when First==10 ->
   score(T, Turn+1, Total+10+element(1,hd(T))+element(2,hd(T)));
 score([{First,Second}|T], Turn, Total) when First+Second==10, Turn==10 ->
   Total + 10 + element(1,hd(T));
 score([{First,Second}|T], Turn, Total) when First+Second==10 ->
   score(T, Turn+1, Total+10+element(1,hd(T)));
 score([{First,Second}|T], Turn, Total) ->
   score(T, Turn+1, Total+First+Second);
 score([], _Turn, Total) ->
   Total.
```  

``` go
package main

import (
    "fmt"

    "github.com/user/newmath"
)

func main() {
    fmt.Printf("Hello, world.  Sqrt(2) = %v\n", newmath.Sqrt(2))
}
```

``` latex
\documentclass[DIV=calc, paper=a4, fontsize=11pt, twocolumn]{scrartcl}   % A4 paper and 11pt font size

\usepackage{lipsum} % Used for inserting dummy 'Lorem ipsum' text into the template
\usepackage[english]{babel} % English language/hyphenation
\usepackage[protrusion=true,expansion=true]{microtype} % Better typography
\usepackage{amsmath,amsfonts,amsthm} % Math packages
\usepackage[svgnames]{xcolor} % Enabling colors by their 'svgnames'
\usepackage[hang, small,labelfont=bf,up,textfont=it,up]{caption} % Custom captions under/above floats in tables or figures
\usepackage{booktabs} % Horizontal rules in tables
\usepackage{fix-cm}  % Custom font sizes - used for the initial letter in the document

\usepackage{sectsty} % Enables custom section titles
\allsectionsfont{\usefont{OT1}{phv}{b}{n}} % Change the font of all section commands

\usepackage{fancyhdr} % Needed to define custom headers/footers
\pagestyle{fancy} % Enables the custom headers/footers
\usepackage{lastpage} % Used to determine the number of pages in the document (for "Page X of Total")

% Headers - all currently empty
\lhead{}
\chead{}
\rhead{}

% Footers
\lfoot{}
\cfoot{}
\rfoot{\footnotesize Page \thepage\ of \pageref{LastPage}} % "Page 1 of 2"

\renewcommand{\headrulewidth}{0.0pt} % No header rule
\renewcommand{\footrulewidth}{0.4pt} % Thin footer rule

```


```  perl
#!/usr/local/bin/perl

open(C, "$ARGV[0]") || die "can't open candidate doc id list file:$ARGV[0]\n";

while (<C>) {
    /([^\s]+)/;
    $dict{$1}=1;
}
close(C);

while (<stdin>) {
    if (/<DOC\s+([^\s>]+)/) {
    $docID = $1;
    } elsif (/<\/DOC>/) {
    if (defined $dict{$docID}) {
        print "<DOC $docID>\n";
        print "$docText\n";
        print "<\/DOC>\n";
    }
    $docText ="";
    $docID ="";
    } else {
    $docText .= $_;
    }
}
```  

```  diff
--- lao Sat Jan 26 23:30:39 1991
+++ tzu Sat Jan 26 23:30:50 1991
@@ -1,7 +1,6 @@
-The Way that can be told of is not the eternal Way;
-The name that can be named is not the eternal name.
 The Nameless is the origin of Heaven and Earth;
-The Named is the mother of all things.
+The named is the mother of all things.
+
 Therefore let there always be non-being,
   so we may see their subtlety,
 And let there always be being,
@@ -9,3 +8,6 @@
 The two are the same,
 But after they are produced,
   they have different names.
+They both may be called deep and profound.
+Deeper and more profound,
+The door of all subtleties!
```  

``` r
# Goal: Experiment with fitting nonlinear functional forms in
#       OLS, using orthogonal polynomials to avoid difficulties with
#       near-singular design matrices that occur with ordinary polynomials.
#       Shriya Anand, Gabor Grothendieck, Ajay Shah, March 2006.

# We will deal with noisy data from the d.g.p. y = sin(x) + e
x <- seq(0, 2*pi, length.out=50)
set.seed(101)
y <- sin(x) + 0.3*rnorm(50)
basicplot <- function(x, y, minx=0, maxx=3*pi, title="") {
  plot(x, y, xlim=c(minx,maxx), ylim=c(-2,2), main=title)
  lines(x, sin(x), col="blue", lty=2, lwd=2)
  abline(h=0, v=0)
}
x.outsample <- seq(0, 3*pi, length.out=100)

# Severe multicollinearity with ordinary polynomials
x2 <- x*x
x3 <- x2*x
x4 <- x3*x
cor(cbind(x, x2, x3, x4))
# and a perfect design matrix using orthogonal polynomials
m <- poly(x, 4)
all.equal(cor(m), diag(4))              # Correlation matrix is I.

par(mfrow=c(2,2))
# Ordinary polynomial regression --
  p <- lm(y ~ x + I(x^2) + I(x^3) + I(x^4))
  summary(p)
  basicplot(x, y, title="Polynomial, insample") # Data
  lines(x, fitted(p), col="red", lwd=3)  # In-sample
  basicplot(x, y, title="Polynomial, out-of-sample")
  predictions.p <- predict(p, list(x = x.outsample))    # Out-of-sample
  lines(x.outsample, predictions.p, type="l", col="red", lwd=3)
  lines(x.outsample, sin(x.outsample), type="l", col="blue", lwd=2, lty=2)
  # As expected, polynomial fitting gives terrible results out of sample.

# These IDENTICAL things using orthogonal polynomials
  d <- lm(y ~ poly(x, 4))
  summary(d)
  basicplot(x, y, title="Orth. poly., insample") # Data
  lines(x, fitted(d), col="red", lwd=3)  # In-sample
  basicplot(x, y, title="Orth. poly., out-of-sample")
  predictions.op <- predict(d, list(x = x.outsample))    # Out-of-sample
  lines(x.outsample, predictions.op, type="l", col="red", lwd=3)
  lines(x.outsample, sin(x.outsample), type="l", col="blue", lwd=2, lty=2)

# predict(d) is magical! See ?SafePrediction
# The story runs at two levels. First, when you do an OLS model,
# predict()ion requires applying coefficients to an appropriate
# X matrix. But one level deeper, the polynomial or orthogonal-polynomial
# needs to be utilised for computing the X matrix based on the
# supplied x.outsample data.
# If you say p <- poly(x, n)
# then you can say predict(p, new) where predict.poly() gets invoked.
# And when you say predict(lm()), the full steps are worked out for
# you automatically: predict.poly() is used to make an X matrix and
# then prediction based on the regression results is done.

all.equal(predictions.p, predictions.op) # Both paths are identical for this
                                         # (tame) problem.
```  

```  matlab
% Create an Automation control object and put it in a figure.
hf = figure;
title('ActiveX Sample Control')
set(gca,'Xtick',[],'Ytick',[],'Box','on')
fp = get(hf,'Position');
mwsampPosition = get(hf,'DefaultAxesPosition').*fp([3 4 3 4]) ;
mwsamp = actxcontrol('MWSAMP.MwsampCtrl.2', mwsampPosition+1, hf)

% Create an Automation server object.
hExcel = actxserver('excel.application')
```  

``` lisp
;; Declare the correct package for this application; 
;; for this example, use the "user" package.
(in-package "USER")

;; Define a default size for the queue.
(defconstant default-queue-size 100 "Default size of a queue")


;;; The following structure encapsulates a queue.  It contains a
;;; simple vector to hold the elements and a pair of pointers to
;;; index into the vector.  One is a "put pointer" that indicates
;;; where the next element is stored into the queue.  The other is
;;; a "get pointer" that indicates the place from which the next
;;; element is retrieved.
;;;
;;; When put-ptr = get-ptr, the queue is empty.
;;; When put-ptr + 1 = get-ptr, the queue is full.
(defstruct (queue (:constructor create-queue)
                  (:print-function queue-print-function))
  (elements #() :type simple-vector)    
                                 ; simple vector of elements
  (put-ptr 0 :type fixnum)       ; next place to put an element
  (get-ptr 0 :type fixnum)       ; next place to take an element
  )


;; To make QUEUE-NEXT efficient, give the Compiler some hints.
(eval-when (compile eval)
  (proclaim '(inline queue-next))
  (proclaim '(function queue-next (queue fixnum) fixnum))
  )


(defun queue-next (queue ptr)
  "Increment a queue pointer by 1 and wrap around if needed."
  (let ((length (length (queue-elements queue)))
        (try (the fixnum (1+ ptr))))
    (if (= try length) 0 try)))

```

```  regex
^(([a-zA-Z]:)|(\\{2}\w+)\$?)(\\(\w[\w].*))(.jpg|.JPG|.gif|.GIF|.doc|.DOC|.pdf|.PDF)$
```  

---

# Bug
```objective-c
//  AppDelegate.m
//  faceAwarenessClipping

#import "AppDelegate.h"
#import "ViewController.h"

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    
    // Override point for customization after application launch.
    if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPhone) {
        self.viewController = [[ViewController alloc] initWithNibName:@"ViewController_iPhone" bundle:nil];
    }
    else {
        self.viewController = [[ViewController alloc] initWithNibName:@"ViewController_iPad" bundle:nil];
    }
    self.window.rootViewController = self.viewController;
    [self.window makeKeyAndVisible];
    return YES;
}

@end

```

# bug
```cpp
static, volatile, int, typedef,
void foo() { }
struct TNode  {
  static, volatile, int, typedef,
  void foo() { };
};
```

# bug
```cpp
// @262
// binder: surface->asBinder()/surfaceTexture->asBinder()
// window: surface/SurfaceTextureClient(surfaceTexture)
status_t CameraClient::setPreviewWindow
```

# bug 

``` latex
\usepackage{lettrine} % Package to accentuate the first letter of the text
\newcommand{\initial}[1]{ % Defines the command and style for the first letter
\lettrine[lines=3,lhang=0.3,nindent=0em]{
\color{DarkGoldenrod}
{\textsf{#1}}}{}}
```
