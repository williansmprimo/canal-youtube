import { Contato } from "./contato-interface";

const contatosURL = 'http://localhost:3001/contatos';

const ContatosService = {
    cadastrar: async (contato: Contato) => fetch(contatosURL,{
        method: 'POST',
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(contato)
    }).then(resposta => resposta.json()),

    listar: async () => fetch(contatosURL, {
        method: 'GET',
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        },
    }).then(resposta => resposta.json())
};

export default  ContatosService;