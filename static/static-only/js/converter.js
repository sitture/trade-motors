function reloadFUXTYkABv()
{
    var sc = document.getElementById("scFUXTYkABv");
    if (sc) sc.parentNode.removeChild(sc);
    sc = document.createElement("script");
    sc.type = "text/javascript";
    sc.charset = "UTF-8";
    sc.async = false;
    sc.id = "scFUXTYkABv";
    sc.src =
        "http://freecurrencyrates.com/en/widget-vertical-editable?iso=GBPMZNUSD&df=2&p=FUXTYkABv&v=fits&source=yahoo&width=300&width_title=0&firstrowvalue=1&thm=A6C9E2,FCFDFD,4297D7,5C9CCC,FFFFFF,C5DBEC,FCFDFD,2E6E9E,000000&tzo=" +
        (new Date()).getTimezoneOffset();
    var div = document.getElementById("gcw_mainFUXTYkABv");
    console.log(div);
    div.parentNode.insertBefore(sc, div);

}
reloadFUXTYkABv();