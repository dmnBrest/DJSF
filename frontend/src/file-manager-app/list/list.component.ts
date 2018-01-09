import { Component, OnInit } from '@angular/core';
import { RemoteActionService } from '../../common/services/remote-action.service';

@Component({
    selector: 'list-component',
    templateUrl: './list.component.html',
    styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {

    constructor(private remoteActionService: RemoteActionService) { }

    ngOnInit() {
        this.remoteActionService.remoteCall();

    }

}
