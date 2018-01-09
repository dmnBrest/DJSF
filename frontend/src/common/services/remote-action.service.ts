import { Injectable } from '@angular/core';

@Injectable()
export class RemoteActionService {

    constructor() { }

    remoteCall():any {
        console.log('REMOTE CALL');
    }

}
