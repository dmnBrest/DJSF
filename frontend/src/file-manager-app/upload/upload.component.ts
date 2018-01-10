import { Component, OnInit, AfterViewInit, ViewChild, ElementRef } from '@angular/core';
import { MessagesService } from '../../common/services/messages.service';

declare var jQuery:any;

@Component({
    selector: 'upload-component',
    templateUrl: './upload.component.html',
    styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit, AfterViewInit {

    @ViewChild('fileinput', {read: ElementRef}) inputEl:ElementRef;
    @ViewChild('uploadButton', {read: ElementRef}) uploadButtonEl:ElementRef;

    constructor(private messagesService: MessagesService) {}

    ngAfterViewInit() {

        jQuery(this.uploadButtonEl.nativeElement).click(() => {
            jQuery(this.inputEl.nativeElement).click();
        });

        jQuery(this.inputEl.nativeElement).fileupload({
            dataType: 'json',
            url: '/file-manager/',
            done: (e, data) => {
                console.log('D:', data)
                this.messagesService.addMessage('SUCCESS', 'File saved successfull. '+data.result.url)
            }
        });

    }

    ngOnInit() {

        // jQuery(".js-upload-photos").click(function () {
        //     jQuery("#fileupload").click();
        // });

        // /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
        // jQuery("#fileupload").fileupload({
        //     dataType: 'json',
        //     done: function (e, data) {
        //         console.log('D:', data)
        //         /*
        //         if (data.result.is_valid) {
        //             $("#gallery tbody").prepend(
        //                 "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
        //             )
        //         }
        //         */
        //     }
        // });
    }

}
