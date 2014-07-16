define(function(require) {
    require('jquery');
    require('bootstrap');
    require('swiper');
    require('django-csrf-support');
    require('velocity');
	$=jQuery.noConflict();
    
	var provet = {
		check_circle:function() {
			var text = $(".circle_num").val();
            var regu = /^\d{3}$/;
	        var re = new RegExp(regu);
            if(text.match(re)){
                return true;
            }
            else {
                return false;
            }
        },
		check_top:function() {
			var text = $(".top_num").val();
			var regu = /^\d{8}$/;
            var re = new RegExp(regu);
            if(text.match(re))	{
				return true;
			}
			else {
				return false;
			}
		},
        check_pro:function(circle,top) {
            //ajax请求接口查询罐码是否正确
            //post过去circle,top
            $.post("//",{
                "circle":circle,
                "top":top
            },function(data){
                if(data.statu=="success")   {
                    return true;
                }
                else {
                    return false;
                }
            });

        },
        check:function(){
            if(provet.check_top()&&provet.check_circle()){
                return true;
            }
            else {
                return false;
            }
        },
        post_pro:function() {
            $.post("/promotion/pro_mobvet/",{
                "circle":$(".circle_num").val(),
                "top":$(".top_num").val()
            },function(data){
                $("html").html(data);
            },"html");
        }
	};
    var mobvet = {
        check_mobile:function() {
            var text = $(".top_num").val();
            var regu = /^\d{13}$/;
            var re = new RegExp(regu);
            if(text.match(re))  {
                return true;
            }
            else {
                return false;
            }
        }
    };
    var postticket = {
        mobticket : function()  {

        },
        proticket : function()  {

        }
    };
    var ajax_window = {
        show_window :function(src) {
            var height = document.documentElement.clientHeight;
            var pop_height ;
            $.get(src,function(data){
                $(".pop-window").html($(data).nextAll("div").html());
                pop_height = $(".pop-window").css("height");
                pop_height = pop_height.substr(0,pop_height.length-2);
                
                height = (height - pop_height)/2;
                $(".pop-window").css({"top":height+"px"});
                
                $(".pop-window").velocity("fadeIn");

            },"html");  
        }
    }
	$(function(){

        //跳转到相应学员
        var mySwiper = new Swiper('.swiper-container',{
            //Your options here:
            loop:true,
            mode:'vertical',
            //etc..
          });  
        
          
		$(".go_check").click(function(){
            if(!provet.check()){
                
                alert("输入不符合规则哦");
            }
            else {
                if(provet.check_pro())  {
                    
                }
            }
        });
        $(".pro_mob_check").click(function(){
            if(!mobvet.check_mobile())  {
                alert("输入不合理");
            }
            else {
                //ajax过去验证并返回结果
                //假设结果为1

            }
        });
        $(".postticket").click(function(){
            if($(this).data("type")=="mob")   {
               /* var id = $(this).data("value");
                $.post("//",{
                    "mobile":mobilenum,
                    "type":"mob",
                    "studentid":id
                },function(data){
                    
                });*/
            }
            else if($(this).data("type")=="pro")  {
                /*var id = $(this).data("value");
                $.post("//",{
                    "pro":mobilenum,
                    "circle":拉环码,
                    "top":罐码,
                    "type":"mob",
                    "studentid":id
                },function(data){
                    
                });*/

            }
        }) ;
       
        $(".instruction_link").click(function(){
            ajax_window.show_window("/promotion/instruction/");
        });
        $(".provet_link").click(function(){
            ajax_window.show_window("/promotion/provet/");
        });
        $(".mobvet_link").click(function(){
            ajax_window.show_window("/promotion/mobvet/");
        });
        
        $(document).on("click",".pop-close",function(){
            $(".pop-window").velocity('fadeOut',function(){
                $(".pop-window").html("");
            });
            
        });
	});
});
