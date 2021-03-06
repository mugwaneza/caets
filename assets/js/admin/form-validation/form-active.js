(function ($) {
 "use strict";
 // Validation for order form
		$(".add-professors").validate(
		{					
			rules:
			{	
				firstname:
				{
					required: true
				},
				lastname:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				},
				username:
				{
					required: true,
					minlength:5,
				},
				password:
				{
					required: true,
					minlength:8,
				},
				categoryname:
				{
					required: true,
				},
				institutionname:
				{
					required: true,
				},
				photo:
				{
					required: true,
				},
				address:
				{
					required: true,
				},
				tel:
				{required: true,
                 minlength:10,
                 maxlength:10,
				},
				servicecat:
				{required: true,
				},
				compcat:
				{required: true,
				},
				institu:
				{required: true,
				},
				servicetype:
				{required: true,
				},
				service_cat:
				{
				required: true,
				},
				dealtitle:
				{
				required: true,
				},
				price:
				{
				required: true,
				},
				servicetypeID:
				{
				required: true,
				},
				provincename:
					{
				required: true,
				},
				district:
					{
				required: true,
				},

				districtname:
					{
				required: true,
				},

				sectorname:
					{
				required: true,
				},
				business:
					{
				required: true,
				},

				phonenumber:
					{
				required: true,
				 minlength:10,
                 maxlength:10,
				},
				pricingclass:
					{
				required: true,

				},
				pricingclass_price:
					{
				required: true,

				}
			},
			messages:
			{	
				firstname:
				{
					required: 'Please enter first name'
				},
				lastname:
				{
					required: 'Please enter last name'
				}
				,
				username:
				{
					required: 'Please enter username'
				},
				password:
				{
					required: 'Please enter password'
				},
				email:
				{
					required: 'Please enter your email address',
				},
				categoryname:
				{
					required: 'Please enter company category',
				},
				institutionname:
				{
					required: 'Please enter institution name',
				},
				photo:
				{
					required: 'Photo is required',
				},
				address:
				{
					required: 'Please enter address',
				},
				tel:
				{
					required: 'Please enter institution phone number',
				},
               servicecat:
				{
					required: 'Please enter service category name',
				},
				compcat:
				{
					required: 'Please select service category',
				},
				institu:
				{
					required: 'Please select  institution name',
				},
				servicetype:
				{
					required: 'Please enter service type',
				},
				service_cat:
				{
					required: 'Please select service category',
				},
				servicetypeID:
				{
					required: 'Please select service type',
				},
               dealtitle:
				{
					required: 'Please enter service deal title',
				},
				price:
				{
					required: 'Please enter price',
				},
				provincename:
				{
					required: 'Province can not be empty',
				},
				district:
				{
					required: 'District can be empty',
				},districtname:
				{
					required: 'District can be empty',
				},
				sectorname:
				{
					required: 'Sector can not be empty',
				},phonenumber:
				{
					required: 'please enter telephone',
				},
				business:
				{
					required: 'please enter business',
				},
				pricingclass:
				{
					required: 'Pricing is required',
				},
				pricingclass_price:
				{
					required: 'Price is required',
				},




			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
 
 // Validation for order form
		$("#acount-infor").validate(
		{					
			rules:
			{	
				email:
				{
					required: true,
					email: true
				},
				phoneno:
				{
					required: true
				},
				password:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				},
				confarmpassword:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				}
			},
			messages:
			{	
			
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				},
				phoneno:
				{
					required: 'Please enter mobile number'
				},
				password:
				{
					required: 'Please enter your password'
				},
				confarmpassword:
				{
					required: 'Please enter your confarm password'
				}
				
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
 
 // Validation for order form
		$(".addcourse").validate(
		{					
			rules:
			{	
				coursename:
				{
					required: true
				},
				finish:
				{
					required: true
				},
				duration:
				{
					required: true
				},
				price:
				{
					required: true
				},
				imageico:
				{
					required: true
				},
				department:
				{
					required: true
				},
				description:
				{
					required: true
				},
				crprofessor:
				{
					required: true
				},
				year:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				},
				phoneno:
				{
					required: true
				},
				password:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				},
				confarmpassword:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				}
			},
			messages:
			{	
				coursename:
				{
					required: 'Please enter course name'
				},
				finish:
				{
					required: 'Please select date of birth'
				},
				duration:
				{
					required: 'Please enter duration'
				},
				price:
				{
					required: 'Please enter price'
				},
				imageico:
				{
					required: 'Please enter image'
				},
				department:
				{
					required: 'Please enter department'
				},
				description:
				{
					required: 'Please enter description'
				},
				crprofessor:
				{
					required: 'Please enter course professor'
				},
				year:
				{
					required: 'Please enter year'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				},
				phoneno:
				{
					required: 'Please enter mobile number'
				},
				password:
				{
					required: 'Please enter your password'
				},
				confarmpassword:
				{
					required: 'Please enter your confarm password'
				}
				
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
		
		
		
 
	// Validation for login form
		$("#comment").validate(
		{					
			rules:
			{	
				name:
				{
					required: true
				},
				message:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				}
			},
			messages:
			{	
				name:
				{
					required: 'Please enter your name'
				},
				message:
				{
					required: 'Please enter your message'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
		
	// Validation for login form
		$(".addlibrary").validate(
		{					
			rules:
			{	
				nameasset:
				{
					required: true
				},
				subject:
				{
					required: true
				},
				imageico:
				{
					required: true
				},
				type:
				{
					required: true
				},
				price:
				{
					required: true
				},
				year:
				{
					required: true
				},
				status:
				{
					required: true
				},
				department:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				}
			},
			messages:
			{	
				nameasset:
				{
					required: 'Please enter your name of assets'
				},
				subject:
				{
					required: 'Please enter your subject'
				},
				imageico:
				{
					required: 'Please enter image'
				},
				department:
				{
					required: 'Please enter your department'
				},
				type:
				{
					required: 'Please enter library type'
				},
				price:
				{
					required: 'Please enter price'
				},
				year:
				{
					required: 'Please enter year'
				},
				status:
				{
					required: 'Please enter status'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
	// Validation for login form
		$(".add-department").validate(
		{					
			rules:
			{	
				name:
				{
					required: true
				},
				headofdepartment:
				{
					required: true
				},
				email:
				{
					required: true
				},
				phone:
				{
					required: true
				},
				noofstudent:
				{
					required: true
				},
				status:
				{
					required: true
				}
			},
			messages:
			{	
				name:
				{
					required: 'Please enter your name'
				},
				headofdepartment:
				{
					required: 'Please enter head of department'
				},
				email:
				{
					required: 'Please enter email'
				},
				phone:
				{
					required: 'Please enter your phone'
				},
				noofstudent:
				{
					required: 'Please enter no of student'
				},
				status:
				{
					required: 'Please enter status'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
	// Validation for login form
		$("#send-mail").validate(
		{					
			rules:
			{	
				name:
				{
					required: true
				},
				headofdepartment:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				},
				phone:
				{
					required: true
				},
				noofstudent:
				{
					required: true
				},
				status:
				{
					required: true
				}
			},
			messages:
			{	
				name:
				{
					required: 'Please enter your name'
				},
				headofdepartment:
				{
					required: 'Please enter head of department'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				},
				noofstudent:
				{
					required: 'Please enter no of student'
				},
				status:
				{
					required: 'Please enter status'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});


		
 
})(jQuery); 