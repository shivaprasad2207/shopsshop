 
$(document).ready(function(){
        var t = $("#div1").load("/templet/navBar.html").text();
        var aa = {};
        var output = Mustache.render(t,aa );
        document.getElementById('div1').innerHTML = output;
});

function onMyClick(){
        var ar ={
                "data": [
                                {
                                        "name": "AAA",
                                        "childs": [
                                                   {
                                                        "link": "//////",
                                                        "name": "AAA-C1"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "AAA-C2"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "AAA-C3"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "AAA-C4"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "AAA-C5"
                                                   }
                                                 ]
                                },
                                {
                                        "name": "BBB",
                                        "childs": [
                                                   {
                                                        "link": "//////",
                                                        "name": "BBB-C1"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "BBB-C2"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "BBB-C3"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "BBB-C4"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "BBB-C5"
                                                   }
                                                 ]
                                },
                                
                                {
                                        "name": "CCC",
                                        "childs": [
                                                   {
                                                        "link": "//////",
                                                        "name": "CCC-C1"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "CCC-C2"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "CCC-C3"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "CCC-C4"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "CCC-C5"
                                                   }
                                                 ]
                                },
                                {
                                        "name": "DDD",
                                        "childs": [
                                                   {
                                                        "link": "//////",
                                                        "name": "DDD-C1"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "DDD-C2"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "DDD-C3"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "DDD-C4"
                                                   },
                                                   {
                                                        "link": "//////",
                                                        "name": "DDD-C5"
                                                   }
                                                 ]
                                },
                                
                                
                        ]
        };
        var t = $("#div2").load("/templet/drop_down.html").text();
        output = Mustache.render(t, ar);
        document.getElementById('div3').innerHTML = output; 

}

function deb(){
        document.getElementById('div4').innerHTML = "BBBBBBBBB";
}