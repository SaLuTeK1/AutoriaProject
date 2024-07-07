import {authService} from "./authService";
import {w3cwebsocket as W3cWebsocket} from 'websocket';
import {socketBaseURL} from "../constants/urls";

const socketService = async () => {
    const {data: {token}} = await authService.getSoketToken();
    return {
        adverts: ()=>new W3cWebsocket(`${socketBaseURL}/adverts/?token=${token}`)
    }
}

export {
    socketService
}