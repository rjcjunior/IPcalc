# IPcalc
O Objetivo deste trabalho foi ser uma ferramenta para a segmentação de sub-redes IPv4 em sub-redes menores.
Ela funciona em 3 modos:

1.Modo de informações: o programa receberá como argumento uma sub-rede IPv4 e imprimirá na tela informações como o endereço de broadcast, e o número máximo de hosts endereçáveis.
2.Modo de divisão em sub-redes menores com prefixo de tamanho fixo: o programa receberá como argumento uma sub-rede IPv4 e um novo tamanho de prefixo e imprimirá informações acerca de todas as sub-redes com o tamanho de prefixo informado que se encontram dentro da sub-rede original.
3.Modo de divisão em sub-redes menores com prefixos variáveis: o programa receberá como argumento uma sub-rede IPv4 e um ou mais valores inteiros informando as quantidades de hosts que devem ser endereçados nas sub-redes menores a serem criadas a partir da sub-rede original. O programa, então, calculará a divisão mais eficiente da sub-rede original nas novas sub-redes e, para cada nova sub-rede gerada, imprimirá uma série de informações.

Uma descrição mais detalhada de como cada modo funciona é encontrado na especificação.
