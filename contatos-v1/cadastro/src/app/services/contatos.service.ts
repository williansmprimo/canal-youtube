import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Contato } from '../models/contato.interface';

@Injectable({
  providedIn: 'root'
})
export default class ContatoService {
    static baseURL = 'http://localhost:3001/contatos';
    constructor(private http: HttpClient){}

    salvar(contato: Contato){
        return this.http.post(ContatoService.baseURL, contato, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
}