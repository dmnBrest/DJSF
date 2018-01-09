import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { ListComponent } from './list/list.component';
import { UploadComponent } from './upload/upload.component';
import { DetailsComponent } from './details/details.component';
import {RemoteActionService} from './../common/services/remote-action.service'


@NgModule({
  declarations: [
    AppComponent,
    ListComponent,
    UploadComponent,
    DetailsComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [RemoteActionService],
  bootstrap: [AppComponent]
})
export class AppModule { }
