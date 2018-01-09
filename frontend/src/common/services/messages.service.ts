import { Injectable } from '@angular/core';

@Injectable()
export class MessagesService {

    constructor() { }

    addMessage(type: string, message: string) {
        console.log(message);
        (window as any).MessagesService.add(type, message);
    }

}
