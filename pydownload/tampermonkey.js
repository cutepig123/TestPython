// ==UserScript==
// @name         Get ebooks.cmanuf.com links
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://ebooks.cmanuf.com/*
// @require      http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    debugger;

    function _x(STR_XPATH) {
        var xresult = document.evaluate(STR_XPATH, document, null, XPathResult.ANY_TYPE, null);
        var xnodes = [];
        var xres;
        while (xres = xresult.iterateNext()) {
            xnodes.push(xres);
        }

        return xnodes;
    }

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async function delayedGreeting() {
        console.log("Hello");
        await sleep(2000);
        console.log("World!");
        await sleep(2000);
        console.log("Goodbye!");
    }

    async function main(){

        //delayedGreeting();

        var n=0;
        var last_book_href='';

        // each page
        for(var i=0; i<100; i++){
            var books = '';

            // check if page is updated
            while(true){
                books = _x('//*[@id="booklist"]/dd/a');

                if(books.length==0)
                    await sleep(2000);

                var book_href = $(books[0]).attr('href');
                if(last_book_href==book_href)
                    await sleep(2000);

                last_book_href=book_href;
                break;

            }

            $(books).each(
                function() {
                    // console.log(this.outerHTML);
                    console.log($(this).attr('href'));
                    n = n+1;
                }
            );
            $(_x('//a[@class="layui-laypage-next"]'))[0].click();

            await sleep(2000);
        }
        return n;
    }

    window.addEventListener('load', function() {
          var checkExist = setInterval(function() {
            //if (main()>0) {
                console.log("Exists!");
				main();
                clearInterval(checkExist);
            //}
        }, 1000); // check every 1s
    }, false);
})();