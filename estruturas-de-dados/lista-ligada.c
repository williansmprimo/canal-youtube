#include <stdio.h>
#include <stdlib.h>

struct ITEM {
    int valor;
    struct ITEM* prox;
};
typedef struct ITEM ITEM;

ITEM* criarITEM(int valor){
    ITEM* item = (ITEM*)malloc(sizeof(ITEM));
    item->valor = valor;
    item->prox = NULL;
    return item;
}

void listar(ITEM* inicio){
    ITEM* atual = inicio;
    while(atual != NULL){
        printf("->(%d)", atual->valor);
        atual = atual->prox;
    }
    printf("\n");
}

ITEM* inserir(ITEM* ultimo, ITEM* novo){
    novo->prox = ultimo->prox;
    ultimo->prox = novo;

    return novo;
}

int main(){
    ITEM* inicio = criarITEM(1);
    ITEM* ultimo = inicio;
    
    ultimo = inserir(ultimo, criarITEM(2));
    ITEM* segundo = ultimo;
    ultimo = inserir(ultimo, criarITEM(5));
    inserir(segundo, criarITEM(3));


    listar(inicio);
    return 0;
}
