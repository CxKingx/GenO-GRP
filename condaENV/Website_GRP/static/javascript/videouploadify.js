// Check character count for 'Artefact Description'
$('#artefact_desc').keyup(function() {
    
    // Initialize variables
    var count = $(this).val().length;
    var current_desc = $('#current_desc');
    var maximum = $('#max_desc');
    var count_desc = $('#count_desc');
      
    current_desc.text(count);
  
    // If word limit (600 chars) is reached, change color to Red
    if (count >= 600) {
      maximum.css('color','#FF0000');
      count_desc.css('color', '#FF0000');
    }
    else {
      maximum.css('color','#787575');
      count_desc.css('color', '#787575');
    }
  
});

/* drag and drop start */
;(function($,window,document,undefined){
	// Prevent issues about browser opening file by dropping it.
	window.addEventListener("dragover",function(e){
		e=e||event;
		e.preventDefault();
	},false);
	window.addEventListener("drop",function(e){
		e=e||event;
		e.preventDefault();
	},false);

	const compareMimeType=(mimeTypes,fileType,formatFile)=>{
		// If accept is defined as *.
		if(mimeTypes.length<2&&mimeTypes[0]==="*"){
			return true;
		}
		// Checking all types written in accept.
		for(let index=1;index<mimeTypes.length;index+=3){
			// image/*, audio/*, video/*
			if(mimeTypes[index+1]==="*"&&fileType.search(new RegExp(mimeTypes[index]))!=-1){
				return true;
			}
			// application/vnd.ms-excel, application/vnd.ms-powerpoint
			else if(mimeTypes[index+1]&&mimeTypes[index+1]!="*"&&fileType.search(new RegExp("\\*"+mimeTypes[index+1]+"\\*"))!=-1){
				return true;
			}
			// application/pdf, image/jpg
			else if(mimeTypes[index+1]&&mimeTypes[index+1]!="*"&&fileType.search(new RegExp(mimeTypes[index+1]))!=-1){
				return true;
			}
			// .jpg, .pdf .png
			else if(mimeTypes[index+1]===""&&(fileType.search(new RegExp(mimeTypes[index]))!=-1||formatFile.search(new RegExp(mimeTypes[index]))!=-1)){
				return true;
			}
		}
		return false;
	}
	// Define the plugin imageuploadify.
	$.fn.videouploadify=function(opts){

		// Override default option with user's if exist.
		const settings=$.extend({},$.fn.videouploadify.defaults,opts);
		// Initialize every element.
		this.each(function(){

			// Save the current element to self to avoid conflict.
			const self=this;

			// Apply on input file having "multiple" attribute only.
			if(!$(self).attr("multiple")){
				return;
			}
			// Save accept files
			let accept=$(self).attr("accept")?$(self).attr("accept").replace(/\s/g,"").split(","):null;
			let result=[];

			// Loop the array of accept files to split all part of mimetype or format.
			accept.forEach((item)=>{
				let regexp;
				// Select the regexp according to the result (mimetype or format)
				if(item.search(/\//)!=-1){
					regexp=new RegExp("([A-Za-z-.]*)\/([A-Za-z-*.]*)","g");
				}
				else{
					regexp=new RegExp("\.([A-Za-z-]*)()","g");
				}
				// Exec the regexp and then 
				const r=regexp.exec(item);
				result=result.concat(r);
			});

			// Array containing all files add by dialog box or drag'n drop.
			let totalFiles=[];
			// Count the number of time a "dragenter" enter the box.
			let counter=0;

			// Define the dragbox layout.
			let dragbox=$(`<div class="videouploadify well">
				<div class="videouploadify-overlay">
					<i class="fa fa-picture-o"></i></div>
					<div class="videouploadify-videos-list text-center">
						<i class="fa fa-cloud-upload"></i>
						<span class='videouploadify-message'>drag & drop video file(s) here to upload</span>
						<button type="button"class="btn btn-default">or select file to upload</button>
					</div>
				</div>`);

			// Save all elements of the dragbox.
			let overlay=dragbox.find(".videouploadify-overlay");
			let uploadIcon=dragbox.find(".videouploadify-overlay i");
			
			let videosList=dragbox.find(".videouploadify-artefacts-list");
			let addIcon=dragbox.find(".videouploadify-artefacts-list i");
			let addMsg=dragbox.find(".videouploadify-artefacts-list span");
			let button=dragbox.find(".videouploadify-artefacts-list button");
			

			/** FUNCTIONS  **/
      		// Function to read and store files.
      		const retrieveFiles=(files)=>{
				for(let index=0;index<files.length;++index){

					//restricting file size
          			if(files[index].size > 5000) {
            			alert("File is too big!");
            			break;
          			}


					if(!accept||compareMimeType(result,files[index].type,/(?:\.([^.]+))?$/.exec(files[index].name)[1])){
						// Unique number to save the image.
						const id=Math.random().toString(36).substr(2,9);
						readingFile(id,files[index]);
						totalFiles.push({
							id:id,file:files[index]
						});
					}
				}
			}

			// Function to read a file.
			const readingFile=(id,file)=>{
				const fReader=new FileReader();
				const width=dragbox.width();
				const boxesNb=Math.floor(width / 100);
				const marginSize=Math.floor((width-(boxesNb*100))/(boxesNb+1));
				// Create the preview file container box.
				let container=$(`<div class='videouploadify-container'>
							<button type='button'class='btn btn-danger glyphicon glyphicon-remove'></button>
							<div class='videouploadify-details'>
								<span>${file.name}</span>
								<span>${file.type}</span>
								<span>${file.size}</span>
							</div>
						</div>`);
				let details=container.find(".videouploadify-details");
				let deleteBtn=container.find("button");
				// Preview file container box CSS
				container.css("margin-left",marginSize+"px");
				// Manage display/hidding details about preview files.
				details.hover(function(){
					$(this).css("opacity","1");
				}).mouseleave(function(){
					$(this).css("opacity","0");
				});
				// If the given file in the parameter is a video
				if(file.type&&file.type.search(/video/)!=-1){
					// Associated function to a ending load
					fReader.onloadend=function(e){
						let video=$("<video>");
						// Paste the image source to display the video preview.
						video.attr("src",e.target.result);
						// Append the image to its container and then the container to the list of files.
            			container.append(video);
						videosList.append(container);
						// Apply left margin to first container of each row and right to last.
						videosList.find(".videouploadify-container:nth-child("+boxesNb+"n+4)").css("margin-left",marginSize+"px");
						videosList.find(".videouploadify-container:nth-child("+boxesNb+"n+3)").css("margin-right",marginSize+"px");
					};
				}
				else if(file.type){
					// Create the generic icon for unknown type file.
					let type="<i class='fa fa-file'></i>";
					if(file.type.search(/audio/)!=-1){
						type="<i class='fa fa-file-audio-o'></i>";
					}
					else if(file.type.search(/image/)!=-1){
						type="<i class='fa fa-file-image-o'></i>";
					}
					fReader.onloadend=function(e){
						let span=$("<span>"+type+"</span>");
						span.css("font-size","5em");
						container.append(span);
						videosList.append(container);
						videosList.find(".videouploadify-container:nth-child("+boxesNb+"n+4)").css("margin-left",marginSize+"px");
						videosList.find(".videouploadify-container:nth-child("+boxesNb+"n+3)").css("margin-right",marginSize+"px");
					};
				}
				// Delete the file from the list.
				deleteBtn.on("click",function(){
					$(this.parentElement).remove();
					for(let index=0;totalFiles.length>index;++index){
						if(totalFiles[index].id===id){
							totalFiles.splice(index,1);
							break;
						}
					}
				});
				fReader.readAsDataURL(file);
			};
			const disableMouseEvents=()=>{
				// Display the overlay and change the dragbox border color.
				overlay.css("display","flex");
				dragbox.css("border-color","#3AA0FF");
				// Disable pointer events to avoid miscapture dragexit children's events.
				button.css("pointer-events","none");
				addMsg.css("pointer-events","none");
				addIcon.css("pointer-events","none");
				videosList.css("pointer-events","none");
			}
			const enableMouseEvents=()=>{
				// Hide the overlay and put back the dragbox border color.
				overlay.css("display","none");
				dragbox.css("border-color","rgb(210, 210, 210)");
				// Enable back pointer events to capture click, hover...
				button.css("pointer-events","initial");
				addMsg.css("pointer-events","initial");
				addIcon.css("pointer-events","initial");
				videosList.css("pointer-events","initial");
			}
			/** EVENTS  */
      		// Change the color background of the button according to the mouse.
			button.mouseenter(function onMouseEnter(event){
				button.css("background","#3AA0FF").css("color","white");
			}).mouseleave(function onMouseLeave(){
				button.css("background","white").css("color","#3AA0FF");
			});
			// When click on the button, simulate click on the original input.
			button.on("click",function onClick(event){
				event.stopPropagation();
				event.preventDefault();
				$(self).click();
			});
			// Manage events to display an overlay when dragover files.
			dragbox.on("dragenter",function onDragenter(event){
				event.stopPropagation();
				event.preventDefault();
				counter++;
				disableMouseEvents();
			});
			// Manage events to hide the overlay when dragout files.
			dragbox.on("dragleave",function onDragLeave(event){
				event.stopPropagation();
				event.preventDefault();
				counter--;
				// If the counter is equal to 0 (means that the files are entirely out of the dragbox).
				if(counter===0){
					enableMouseEvents();
				}
			});
			// Manage events when dropping files.
			dragbox.on("drop",function onDrop(event){
				event.stopPropagation();
				event.preventDefault();
				enableMouseEvents();
				// Retrieve the dragged files.
				const files=event.originalEvent.dataTransfer.files;
				// Read all files (to add them to the preview and push them to the files list to submit).
        		retrieveFiles(files);
			});

			// Binding resize event to the window.
			$(window).bind("resize",function(e){
				window.resizeEvt;
				$(window).resize(function(){
					clearTimeout(window.resizeEvt);
					// Compute and change the margin according to the size of the window after 0.5 seconds after resizing.
          window.resizeEvt=setTimeout(function(){
						const width=dragbox.width();
						const boxesNb=Math.floor(width / 100);
						const marginSize=Math.floor((width-(boxesNb*100))/(boxesNb+1));
						// Reset all margins of containers boxes.
						let containers=videosList.find(".videouploadify-container");
						for(let index=0;index<containers.length;++index){
							$(containers[index]).css("margin-right","0px");
							$(containers[index]).css("margin-left",marginSize+"px");
						}
						videosList.find(".videouploadify-container:nth-child("+boxesNb+"n+4)").css("margin-left",marginSize+"px");
						videosList.find(".videouploadify-container:nth-child("+boxesNb+"n+3)").css("margin-right",marginSize+"px");
					},500);
				});
			})

			// Detect when adding files through the dialog box to preview those files and add them to the array.
			$(self).on("change",function onChange(){
				const files=this.files;retrieveFiles(files);
			});
			// When submitting the form.
			$(self).closest("form").on("submit",function(event){
				// Stop the original submit.
				event.stopPropagation();
				event.preventDefault(event);
				// Retrieve all form inputs.
				const inputs=this.querySelectorAll("input, textarea, select, button");
				// Create a form.
				const formData=new FormData();
				// Add all data to the form (selected options, checked inputs, etc...).
				for(let index=0;index<inputs.length;++index){
					if(inputs[index].tagName==="SELECT"&&inputs[index].hasAttribute("multiple")){
						const options=inputs[index].options;
						for(let i=0;options.length>i;++i){
							if(options[i].selected){
								formData.append(inputs[index].getAttribute("name"),options[i].value);
							}
						}
					}
					else if(!inputs[index].getAttribute("type")||((inputs[index].getAttribute("type").toLowerCase())!=="checkbox"&&(inputs[index].getAttribute("type").toLowerCase())!=="radio")||inputs[index].checked){
						formData.append(inputs[index].name,inputs[index].value);
					}
					else if($(inputs[index]).getAttribute("type") !="file"){
						formData.append(inputs[index].name,inputs[index].value);
					}
				}
				// Add all files get from the dialog box or drag'n drop,
				for(var i=0;i<totalFiles.length;i++){
					formData.append(self.name,totalFiles[i].file);
				}
				// Create an request and post all data.
				var xhr=new XMLHttpRequest();
				// When the request has been successfully submitted, redirect to the location of the form.
        		xhr.onreadystatechange=function(e){
					if(xhr.status==200&&xhr.readyState===XMLHttpRequest.DONE){
						window.location.replace(xhr.responseURL);
					}
				}
				xhr.open("POST",$(this).attr("action"),true);
				xhr.send(formData);
				return false;
			});
			// Hide the original input.
			$(self).hide();
			dragbox.insertAfter(this);
		});
		// Return "this" to ensure that chaining methods can be called.
		return this;
	};
	// Default configuraiton of the plugin.
	$.fn.videouploadify.defaults={};
}(jQuery,window,document));
//drag and drop end
// website: https://www.jqueryscript.net/form/Drag-And-Drop-File-Uploader-With-Preview-Imageuploadify.html


document.getElementById('title').addEventListener('blur', validateTitle);

// Project title must be between 4 to 150 characters
function validateTitle() {
  const title = document.getElementById('title');
  // Title can contain alphabets, numbers, and symbols
  const re =  /^[a-zA-Z0-9"';()-_. ]{4,150}/

  if(!re.test(title.value)){
      title.classList.add('is-invalid');
      document.getElementById('submit').disabled = true;
  }
  else {
      title.classList.remove('is-invalid');
      document.getElementById('submit').disabled = false;
  }
}