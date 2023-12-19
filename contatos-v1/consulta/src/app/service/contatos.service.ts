import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Contato } from '../model/contato.interface';

@Injectable({
  providedIn: 'root'
})
export default class ContatoService {
    static baseURL = 'http://localhost:3001/contatos';
    constructor(private http: HttpClient){}

    listar(){
        return this.http.get<Contato[]>(ContatoService.baseURL, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
}