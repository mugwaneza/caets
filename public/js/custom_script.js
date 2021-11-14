
  $(".BtnFilter").click(function() {  // When filter button is clicked
        // hide default page contents
            $(".pagecontent").hide();
           // show  searched results

        $.ajaxSetup({
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            }
        });
        $maxamount = $(".maxamount").val();                                                   // get user input from the form
        $minamount = $(".minamount").val();
    });

$(".price-range").slider({  // when slide bar is released
    start: function(event, ui) {
        // do something on mousedown on slider
    },
    stop: function(event, ui) {      // search for product

        $maxamount = $(".maxamount").val();                                                   // get user input from the form
        $minamount = $(".minamount").val();
        $servicecatname = $(".servicedata").val();
        $('.page_result').empty(" ");

         $.ajax({
            type: "GET",
            url: "/filter/" + $minamount +'/'+ $maxamount + '/'+ $servicecatname,
            async: false,
            dataType: 'json',
            success: function (data) {
               // hide default page contents
                                 $(".pagecontent").hide();
                                 $(".page_result").show();
                                 console.log(data);

             var html = '<div class="row">';
               if (data !="") {


                 data.forEach(function (svcrequirement_data) {
                     svcrequirement_data.service_type.forEach(function (servicetype) {
                         servicetype.service_category.forEach(function (servicecategory) {

                             html += '<div class="col-lg-4 col-sm-6">';
                             html += '<div class="product-item">';
                             html += '<div class="pi-pic">';
                             html += '<div class="pi-pic">';
                             html += '<div class="row gallery" >';
                             if (servicetype.photo != null) {
                                 html +='<img src= '+ servicetype.photo +' alt="photo" data-slide-to="0" class="img-responsive myimage" id='+servicetype.id+' >';

                             } else {
                                 //when service type photo is not there
                                 if (servicetype.cover_photo != null) {
                                 html +='<img src= '+ servicetype.cover_photo +'  alt="photo" data-slide-to="0" class="img-responsive myimage" id='+servicetype.id+' >';
                                 }
                             }
                             html += '</div>';
                             html += '<div class="icon"> <i class="icon_heart_alt"></i> </div><ul>';
                             html += '<li class="w-icon active"><a href="#"><i class="icon_cart_alt"></i> Reserve</a></li>';

                             html += '<li class="w-icon detailslinkd"><a href="#" id='+servicetype.id +'>Details</a></li>';
                             html += ' <li class="quick-view"><a href='+ svcrequirement_data.external_url +' target="_blank"><i class="fa fa-internet-explorer"></i></a></li>';
                             html += '</ul> </div> <div class="pi-text">';
                             html += '<div class="catagory-name text-xl-center">' ;
                                  if(servicecategory.institution_name !=null ){
                             html += '<h6 style="font-family: math; font-size: small;" >'+ servicetype.type_name  +'-'+ servicecategory.institution_name + '</h6>';
                                  }else{
                             html += '<h6 style="font-family: math; font-size: small;" >'+ servicetype.type_name  +'-'+  servicecategory.business.institution + '</h6>';
                                  }
                               html +=  '</div>';
                               html +=  '<hr>';
                               html += '<div class="address" style="font-size: small;">' +
                                   '<span class="fa fa-map-marker text-success " id="location">' +servicecategory.business.sector.sector +'-'+
                                           servicecategory.business.sector.district.district +'-'+
                                          servicecategory.business.sector.district.province.province +' of Rwanda';

                             html += '</span> </div></div> </div> </div></div>';

                         });
                     });
                 });

                 html += '</div>';
                 $('.page_result').append(html);
             }else{

                   html += '<div class="offset-3"> <p class=" mt-5 text-warning "> No information available</p>';
                   html += '</div>';
                   html += '</div>';
                 $('.page_result').append(html);
             }
               },
           error: function (error) {
                console.log(error);
            }
        });

    }});


 $( document ).ready(function () {            // When page loads list all service types that are in that category that was clicked
     $servicecatname = $.trim($(".servicedata").val());


     $.ajax({
         type: "GET",
         url: "/filter/servicecat/"+$servicecatname,
         async: false,
         dataType: 'json',
         success: function (data) {
              data.forEach(function (service) {
                       var   html = '<option value="'+ service.type_name +'">'+ service.type_name +'</option>';
                      $('.datasorting').append(html);
                    });
            }
         })
      })

$(".datasorting").change(function () {      // When sort option is selected get all servicetype name in that cathegory

    var servicetypename = $(this).children("option:selected").val();    //listed service type of selected service cat
    if (servicetypename ==''){

            location.reload(true);

     }else{

         $servicecatname = $(".servicedata").val();           //service category that is first visited and hidden
         $('.page_result').empty(" ");

         $.ajax({
            type: "GET",
            url: "/filter/servicetype/"+ servicetypename + '/'+ $servicecatname,
            async: false,
            dataType: 'json',
                    success: function (data) {
               // hide default page contents
                                 $(".pagecontent").hide();
                                 $(".page_result").show();

              var html = '<div class="row">';

               if (data !="") {
                 data.forEach(function (svcrequirement_data) {
                     svcrequirement_data.service_type.forEach(function (servicetype) {
                         servicetype.service_category.forEach(function (servicecategory) {

                             html += '<div class="col-lg-4 col-sm-6">';
                             html += '<div class="product-item">';
                             html += '<div class="pi-pic">';
                             html += '<div class="pi-pic">';
                             html += '<div class="row gallery" >';
                             if (servicetype.photo != null) {
                                 html +='<img src= '+ servicetype.photo +' alt="photo" data-slide-to="0" class="img-responsive myimage" id='+servicetype.id+' >';

                             } else {
                                 //when service type photo is not there
                                 if (servicetype.cover_photo != null) {
                                 html +='<img src= '+ servicetype.cover_photo +'  alt="photo" data-slide-to="0" class="img-responsive myimage" id='+servicetype.id+' >';
                                 }
                             }
                             html += '</div>';
                             html += '<div class="icon"> <i class="icon_heart_alt"></i> </div><ul>';
                             html += '<li class="w-icon active"><a href="#"><i class="icon_cart_alt"></i> Reserve</a></li>';

                             html += '<li class="w-icon detailslinkd"><a href="#" id='+servicetype.id +'>Details</a></li>';
                             html += ' <li class="quick-view"><a href='+ svcrequirement_data.external_url +' target="_blank"><i class="fa fa-internet-explorer"></i></a></li>';
                             html += '</ul> </div> <div class="pi-text">';
                             html += '<div class="catagory-name text-xl-center">' ;
                                  if(servicecategory.institution_name !=null ){
                             html += '<h6 style="font-family: math; font-size: small;" >'+ servicetype.type_name  +'-'+ servicecategory.institution_name + '</h6>';
                                  }else{
                             html += '<h6 style="font-family: math; font-size: small;" >'+ servicetype.type_name  +'-'+  servicecategory.business.institution + '</h6>';
                                  }
                               html +=  '</div>';
                               html +=  '<hr>';
                               html += '<div class="address" style="font-size: small;">' +
                                   '<span class="fa fa-map-marker text-success " id="location">' +servicecategory.business.sector.sector +'-'+
                                           servicecategory.business.sector.district.district +'-'+
                                          servicecategory.business.sector.district.province.province +' of Rwanda';

                             html += '</span> </div></div> </div> </div></div>';

                         });
                     });
                 });

                 html += '</div>';
                 $('.page_result').append(html);
             }else{

                   html += '<div class="offset-3"> <p class=" mt-5 text-warning "> No information available</p>';
                   html += '</div>';
                   html += '</div>';
                 $('.page_result').append(html);
             }
               },
           error: function (error) {
                console.log(error);
            }
         });

        }
    });
   

  //  Load more button on services page
        $( document ).ready(function () {

        $(".moreBox").slice(0, 6).show();
        $(".loadMore").on('click', function (e) {
        e.preventDefault();

        $(".moreBox:hidden").slice(0, 6).slideDown();
        if ($("moreBox:hidden").length == 0) {
            $(".loadMore").fadeOut('slow');
        }
        $('html,body').animate({
            scrollTop: $(this).offset().top
        }, 1500);

        $('.totop').show();
        });


          // Go back to the top button
        $('a[href=#top]').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 600);
        return false;
        });

        $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('.totop a').fadeIn();
        } else {
            $('.totop a').fadeOut();
        }
       });
        });

    // #Modal image  when image is clicked
       $(".gallery").click(function() {

       var $typeid  =    $(this).closest('.gallery').find('img').attr('id');
        $.ajax({
                type: "GET",
                url: "/filter/by/typeid/"+$typeid,
                async: false,
                dataType: 'json',
                success: function (data) {

              if (data !="") {
                 data.forEach(function (svcrequirement_data) {
                     svcrequirement_data.service_type.forEach(function (servicetype) {
                         servicetype.service_category.forEach(function (servicecategory) {

                        if (servicetype.photo != null) {
                         $('#imagepreview').attr('src',servicetype.photo).val(); // here asign the image to the modal when the user click the enlarge link

                         }
                         else {
                            //when service type photo is not there
                            if (svcrequirement_data.cover_photo != '') {
                           $('#imagepreview').attr('src', svcrequirement_data.cover_photo).val();   //Add image to the  details modal
                            }
                          }
                         });
                         });
                         });
                       }
                   }
                });
        $('#imagemodal').modal('show'); // imagemodal is the id attribute assigned to the bootstrap modal, then i use the show function
    });



      $('.detailslink').click(function() {  // Get service type details when details button is clicked

           var $typeid  =    $(this).closest('.detailslink').find('a').attr('id');
        $.ajax({
                type: "GET",
                url: "/filter/by/typeid/"+$typeid,
                async: false,
                dataType: 'json',
                success: function (data) {

              if (data !="") {
                 data.forEach(function (svcrequirement_data) {
                     svcrequirement_data.service_type.forEach(function (servicetype) {
                         servicetype.service_category.forEach(function (servicecategory) {

                        if (servicetype.photo != null) {
                            $('#preview_imgdetail').attr('src', servicetype.photo).val();   //Add image to the  details modal
                         }
                         else {
                            //when service type photo is not there
                            if (svcrequirement_data.cover_photo != '') {
                           $('#preview_imgdetail').attr('src', svcrequirement_data.cover_photo).val();   //Add image to the  details modal
                            }
                          }

                         if (servicecategory.business.institution !="") {     // Institution or business name

                           $('#pre_typenameid').text(servicetype.type_name + "-" + servicecategory.business.institution);

                           }else{
                          $('#pre_typenameid').text(servicetype.type_name + "-" + servicecategory.institution_name.institution);
                         }

                             $('#pre_location').text(   servicecategory.business.sector.sector  + "-" +
                                           servicecategory.business.sector.district.district + "-" +
                                           servicecategory.business.sector.district.province.province +" Province" );   // business address

                          $('#pre_aboutid').text(svcrequirement_data.about_service);     // about service


                       if (svcrequirement_data.off_price !=""){
                       $('#pre_price').text(svcrequirement_data.pricing_class +" "+svcrequirement_data.price+"Rwf ").append("<del>" + svcrequirement_data.off_price + "Rwf</del>");
                       }else {
                      $('#pre_price').text(svcrequirement_data.pricing_class +" "+ svcrequirement_data.price+ "Rwf");
                       }


                         });
                         });
                         });
                }
                }
              });

        $('#detailsmodal').modal('show'); // detailsmodal show


            });



  $('.aboutmodal').on('click', function(e){
      e.preventDefault();
              $('#Aboutmodal').modal('show'); // detailsmodal show

    });





