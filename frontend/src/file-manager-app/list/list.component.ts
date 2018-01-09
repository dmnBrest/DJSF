import { Component, OnInit } from '@angular/core';
import { RemoteActionService } from '../../common/services/remote-action.service';
import { MessagesService } from '../../common/services/messages.service';

@Component({
    selector: 'list-component',
    templateUrl: './list.component.html',
    styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {

    constructor(
        private remoteActionService: RemoteActionService,
        private messagesService: MessagesService
    ) { }

    ngOnInit() {
        this.remoteActionService.remoteCall();
        this.messagesService.addMessage('INFO', 'Doom Doom')
    }

}
