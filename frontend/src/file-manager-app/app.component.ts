import { Component } from '@angular/core';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css'],

})
export class AppComponent {
    mode = 'list';

    showList() {
        console.log('Show List');
        this.mode = 'list';
        this.getDocuments();
    }

    showUpload() {
        console.log('Show upload');
        this.mode = 'upload';
    }

    getDocuments() {
        console.log('Get Documents');
    }

}
