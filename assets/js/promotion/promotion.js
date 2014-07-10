define(function(require) {
    require('jquery');
    require('bootstrap');
    require('swiper');
    require('django-csrf-support');
	$=jQuery.noConflict();
	var provet = {
		"check_circle":function() {
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
		"check_top":function() {
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
        "check":function(){
            if(provet.check_top()&&provet.check_circle()){
                return true;
            }
            else {
                return false;
            }
        }
	};
    var Vboard = {
        "get_Json" : function()  {

        },
        "change_pic": function()    {
            var mySwiper = new Swiper('.swiper-container',{
            //Your options here:
            mode:'vertical',
            loop: true
            //etc..
          });  
        }
    };
	$(function(){
      $(".student .avatar").css({
          "height":$(".student .avatar").css("width")
      });   
		$(".go_check").click(function(){
            if(!provet.check()){ß
                   
            }
        });
        Vboard.change_pic();    
        
        },
        "post_to_check_num":function(){
            $.post("",{
                "circle":$(".circle_num").val(),
                "top":$(".top_num").val()
            },function(data){
                if(data.back=='success'){
                    location.href="/promotion/mobvet/";
                }
                else {
                    location.href="/promotion/proerror/";
                }
            });
        }
	};
	$(function(){
		$(".go_check").click(function(){
            if(porvet.check()){
                porvet.post_to_check_num(); 
            }
            else {
                
            }
        });
		
	});
});
