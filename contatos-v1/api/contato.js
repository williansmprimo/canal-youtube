mongoose = require('mongoose');

Contato = mongoose.model('Contato', {
    id: Number,
    nome: String,
    telefone: String
});

module.exports = Contato;