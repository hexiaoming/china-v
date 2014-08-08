define(function(require){
    
    require("jquery");
    require("juicer");
    
    
    $(function(){
        onVote();
    });
    
    
    function getVotes(){
        return $.get("votes/backend/data",{},"json");
    }
    
    function onVote(){
        
        function getVotes(){
            return $.get("/votes/backend/data",{},"json");
        }
        
        function makehtml(){
                getVotes().then(function(data){
                    var jsObject = eval(data);
                    var tpl = document.getElementById('tpl').innerHTML;
                    for(var i=jsObject.data.length-1;i>=0;i--)
                    {
                        var temp = {};
                        temp.name = jsObject.data[i].name;
                        var list = new Array();
                        var temp1 = {};
                        temp.width = jsObject.data[i].option.length * 70;
                        for(var j=0;j<jsObject.data[i].option.length;j++)
                        {
                            temp1.name = jsObject.data[i].option[j].name;
                            temp1.image = jsObject.data[i].option[j].image;
                            temp1.values = Number(jsObject.data[i].option[j].votes);
                            list[j] = temp1;
                            temp1 = {};
                        }
                        temp.list = list;
                        console.log(temp);
                        var html = juicer(tpl,temp);
                        $("#rank").append(html);
                    } 
                });
            }
       makehtml();
    }
});
