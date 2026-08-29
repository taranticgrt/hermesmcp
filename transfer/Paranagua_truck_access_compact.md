# Paranaguá Truck Access — Compact Evidence Index

Deterministic extraction of passages that **materially establish** a truck/vehicle gate-access function or the linkage of a named software/system to that function. Verbatim source snippets; no summarising, no paraphrase. Each gathered line carries its original source line number (`L<n>|  <verbatim source text>`).

- **Source filename:** PortX_Paranagua_FULL_RESTRUCTURED_2026-08-29_(2).md
- **Source SHA-256:** `6c1f8b36ec0fb63337319fd58829fa52e559917a6908ea3b07bc397d520f61d8`
- **Source path:** transfer/PortX_Paranagua_FULL_RESTRUCTURED_2026-08-29_(2).md
- **Source lines:** 35425
- **Scope:** passages that materially establish one of: truck/vehicle gate access control; truck appointment/scheduling; vehicle/driver credentialing; OCR/ANPR/LPR/license-plate capture; RFID/tag access; weighing/scale used for entry/exit control; gate automation; triage/regulator-yard admission; explicit named-software attribution to those functions.
- **Excluded:** generic references to Receita, TOS, hinterland, queues, trucks or terminals, unless directly supporting access control or software attribution; PortX-proposed (not-established) canonical event models; data-request / "what PortX should ask" boilerplate; pure reference-document lists.

The functions map onto the dossier's own sections: **5.4** = gate access control / credentialing / RFID+tag / SEV appointment; **5.5** = weighing/scale entry-exit control, UHF/RFID+tag, Guardian queue/yard (incl. agendamento); **5.6** = OCR/ANPR/LPR/license-plate capture; **5.7 / 5.7A** = triage / regulator-yard (Pátio de Triagem) admission.

---

# 5.4 — GATES / CONTROLE DE ACESSO

### 5.4.CEL-2026-B — APPAWeb ↔ RFID / cancelas / ambiente ISPS (L27528)
> L27530| O pacote CELEPAR 2026 descreve o **APPAWeb — Sistema de Operações Portuárias** como integrado à solução de segurança do **ISPS Code**, citando explicitamente **RFID** e **cancelas** no contexto de controle de acesso e liberação de cargas.
> L27534| `APPAWeb (decisão/dados de acesso)` ↔ `ambiente ISPS / RFID / cancelas` ↔ `controladores/dispositivos físicos`.
> L27536| **Limite de evidência:** o contrato prova integração funcional, mas não identifica leitor RFID, frequência/tecnologia, PLC/controlador de cancela, middleware, protocolo ou endpoint. APPAWeb continua **não sendo o controlador físico** da cancela.

### 5.4.CEL-2026 — APPAWeb ↔ ambiente ISPS (L27538)
> L27540| O pacote CELEPAR 2026 caracteriza **APPAWeb — Sistema de Operações Portuárias** como aplicação que suporta **controle de acesso e liberação de cargas** e que é **integrada à solução de segurança do ISPS Code**, incluindo no escopo funcional referências a RFID, cancelas e OCR.
> L27544| `APPAWeb (dados/decisão operacional) ↔ ambiente de segurança ISPS → RFID / cancelas / OCR / controle de acesso físico`.
> L27546| Isso **não autoriza** afirmar que APPAWeb controle diretamente PLCs/cancelas, nem identifica protocolo, middleware ou produto ISPS específico. Para esta interface:

### 5.4.1 Conclusão principal — arquitetura de acesso em seis camadas (L27555)
> L27561| 1. **SICS** — credenciamento/compliance de empresas, pessoas e veículos;
> L27562| 2. **APPAWeb / SEV** — autorização e agendamento de determinados acessos veiculares;
> L27563| 3. **Ronda Senior** — sistema central de controle de acesso físico atualmente contratado;
> L27564| 4. **totens/catracas/torniquetes/leitores** — execução física de identificação;
> L27565| 5. **RFID + OCR + biometria** — mecanismos de autenticação/identificação;
> L27566| 6. **Guarda Portuária / vigilância** — camada humana de segurança, revista e exceções.

### 5.4.2 Sistema atual central: Ronda Senior (L27580)
> L27584| **Contrato 027/2026-APPA — MD Sistemas de Computação Ltda.**
> L27588| - licenças de software para operação do **Ronda Senior**;
> L27605| A página de Contratos Gerais afirma explicitamente que se trata do:
> L27606| **“sistema de controle de acesso Ronda Senior”**.
> L27603| **Confirmado atual 2026.**

### 5.4.3 Licitação atual do Ronda Senior (L27610)
> L27614| **Processo SAP / Edital: 1000000332**
> L27617| **“Licenças, suporte e manutenção do sistema Ronda Senior.”**
> L27631| Portanto, ao contrário do contrato emergencial anterior, o ciclo atual de 24 meses decorre de licitação competitiva.

### 5.4.4 Contrato-ponte emergencial de 2025 (L27635)
> L27639| **Contrato 076/2025-APPA — MD Sistemas de Computação Ltda.**
> L27646| - sustentação da solução de controle de acesso **Ronda Senior**;
> L27647| - suporte 24/7;
> L27648| - prestado por representante nível **Diamante** da Senior.
> L27664| `Inteligate / Totens até 2026`
> L27665| \+
> L27666| `Ronda Senior existente`
> L27667| → `MD Sistemas contrato emergencial 076/2025`
> L27668| → `licitação 1000000332`
> L27669| → `MD Sistemas contrato 027/2026 por 24 meses`.

### 5.4.6 Histórico da solução — 2021 Inteligate (L27695 / L27714)
> L27722| - leitores Mifare;
> L27723| - comunicação TCP/IP;
> L27724| - biometria digital.

### 5.4.7 Totens — locais atendidos (L27745)
> L27747| O contrato Inteligate lista explicitamente os ambientes:
> L27754| Logo, a “Solução de Totens” não era restrita ao gate principal.

### 5.4.8 Tecnologias locais confirmadas (L27760)
> L27764| - **Mifare**
> L27765| - **TCP/IP**
> L27766| - **reconhecimento biométrico digital**
> L27770| - **TAG RFID do veículo**
> L27771| - **OCR da placa**
> L27772| - **biometria do condutor**
> L27776| - código de barras;
> L27777| - cancelas;
> L27778| - CFTV;
> L27779| - catracas;
> L27780| - torniquetes;
> L27781| - leitores biométricos.

### 5.4.9 Regra atual de abertura da cancela (L27787) — gate automation
> L27793| 1. leitura da **TAG RFID**;
> L27794| 2. confirmação da placa via **OCR**;
> L27795| 3. confirmação biométrica do **condutor**;
> L27796| 4. confirmação do credenciamento/autorização correspondente.
> L27800| `vehicle RFID valid`
> L27801| AND
> L27802| `plate OCR match`
> L27803| AND
> L27804| `driver biometric match`
> L27805| AND
> L27806| `access authorization valid`
> L27807| → `gate open`.

### 5.4.13 OCR de acesso — fornecedor histórico Toledo (L27875)
> L27896| Isso confirma Toledo como fornecedor histórico de OCR nos gates/recintos.
> L27901| Toledo continua atual em pesagem/Guardian, mas isso é outro contrato/escopo.

### 5.4.14 Gate vs balança — não misturar OCRs → Automação de pesagem (L27905 / L27916)
> L27918| - veículo;
> L27919| - balança;
> L27920| - rota;
> L27921| - pesagem.

### 5.4.15 APPAWeb / SEV — gate event API real (L27930) — software attribution + appointment
> L27934| `POST /appawebservices/api/ControleAcesso/TCP/Agendamento/Acesso`
> L27938| - `codigoBarras`;
> L27939| - `numSev`;
> L27940| - condutor;
> L27941| - `gate`;
> L27942| - `peso`;
> L27943| - `dataEvento`;
> L27944| - `sentido`.

### 5.4.16 Gates nomeados na documentação APPAWeb (L27955) — named gate IDs
> L27957| Na integração TCP aparecem identificadores como:
> L27959| - `P16`
> L27960| - `GATE_TCP`
> L27961| - `GATE_BITREM`
> L27962| - `PA1`
> L27966| - **Gate 2 / Prédio Dom Pedro II**.
> L27974| Mas provam que o modelo digital possui gate/checkpoint ID.

### 5.4.20 Ronda Senior — dispositivos compatíveis (L28069)
> L28075| - Mifare 13.56 MHz;
> L28076| - 125 kHz;
> L28077| - HID;
> L28078| - fingerprint;
> L28079| - 1:1 e 1:N;
> L28080| - online/offline;
> L28081| - eventos de acesso armazenados;
> L28082| - comunicação **TCP/IP**.

### 5.4.21 Digicon — evidência patrimonial APPA (L28094)
> L28098| **DIGICON MCAACESSO**

### 5.4.25 Mifare — credencial física confirmada (L28184) — credentialing
> L28186| Além do contrato Inteligate, APPA possui histórico de aquisição de:
> L28187| **SmartCard Mifare 1K**.
> L28189| Portanto:
> L28190| Mifare não é apenas capability do Ronda.

### 5.4.26 Torniquetes / catracas (L28196) — physical identification
> L28200| - **13 torniquetes bidirecionais**;
> L28201| - hand-keys para cadastro biométrico.
> L28209| Modelo dos torniquetes:
> L28210| **não fechado nesta rodada**.

### 5.4.27 Sistema de acesso antes do Ronda atual (L28214)
> L28224| **Camada física de Totens**
> L28225| `Senior — Solução de Totens 004/2017`
> L28226| → `Inteligate — manutenção dos Totens 044/2021 (2021–2026)`.
> L28228| **Camada OCR/acesso**
> L28229| `Toledo — OCR de acesso 007/2017`, com continuidade contratual específica posterior não comprovada.
> L28231| O hardware físico possui vida útil e contratos diferentes do software. Em 2025–2026, **MD Sistemas e Inteligate operaram em paralelo**, com escopos distintos.

### 5.4.28 Relação SICS ↔ Ronda (L28237)
> L28243| - credencia;
> L28244| - valida documentação;
> L28245| - perfis;
> L28246| - pessoas;
> L28247| - veículos;
> L28248| - compliance.
> L28252| - mantém permissões;
> L28253| - dispositivos;
> L28256| - eventos;
> L28257| - presença física.
> L28259| A integração funcional é inevitável.
> L28263| - endpoint SICS;
> L28264| - job de sincronização;
> L28265| - mapping;
> L28266| - middleware;

### 5.4.29 Relação APPAWeb/SEV ↔ Ronda (L28275)
> L28279| - cria SEV;
> L28280| - recebe eventos de determinados checkpoints;
> L28281| - conhece motorista/veículo/gate.
> L28291| - APPAWeb envia autorização ao Ronda;
> L28292| - Ronda chama APPAWeb;
> L28293| - ambos consultam uma terceira base;
> L28294| - Gate TCP integra diretamente com APPAWeb fora do Ronda.

### 5.4.30 Relação Ronda ↔ SICS tecnicamente plausível (L28301)
> L28314| B)
> L28315| `Ronda Concentradora → SICS`
> L28316| para validar acesso online.

### 5.4.31 Current vendor/support boundary (L28329) — software attribution
> L28331| | Camada | Vendor/owner atual melhor suportado |
> L28332| |-|-|
> L28333| | credenciamento | APPA/Celepar — SICS |
> L28334| | autorização SEV | APPAWeb |
> L28335| | controle de acesso | Senior Ronda |
> L28336| | suporte Ronda | MD Sistemas |
> L28337| | fabricante Ronda | Senior Sistemas |
> L28338| | manutenção Totens anterior | Inteligate |
> L28339| | OCR acesso histórico | Toledo |
> L28340| | biometria/totens histórico | Senior/Inteligate ecosystem |
> L28341| | segurança humana | APPA/UASP + vigilância contratada |
> L28342| | pesagem | Toledo/Guardian |

### 5.4.32 Contratos e procurement — mapa consolidado (L28346)
> L28348| | Instrumento | Ano | Fornecedor | Escopo | Valor |
> L28349| |-|-|-|-|-|
> L28350| | 004/2017 | 2017 | Senior Sistemas | Solução de Totens | R\$ 1.397.056,31 |
> L28351| | 007/2017 | 2017 | Toledo | OCR de acesso | R\$ 8.146.724,37 |
> L28352| | 044/2021 | 2021 | Inteligate | manutenção Totens/Mifare/TCP-IP/biometria | R\$ 1,10 mi inicial |
> L28353| | 076/2025 | 2025 | MD Sistemas | sustentação emergencial Ronda | R\$ 539.383,40 |
> L28354| | 1000000332 | 2025/26 | licitação | Ronda licenças/suporte/manutenção | R\$ 2.768.696,04 |
> L28355| | 027/2026 | 2026 | MD Sistemas | Ronda 24x7 + licenças + customização | R\$ 2.768.696,04 |
> L28356| | LE303/2025 | 2025/26 | processo licitatório | vigilância/controle humano de acesso | valor conforme contratação final |

### 5.4.33 Dados disponíveis potencialmente para PortX (L28360) — system data model
> L28374| - RFID/card;
> L28375| - placa;
> L28376| - gate;
> L28377| - SEV;
> L28378| - barcode;
> L28379| - composição veicular.
> L28383| - device ID;
> L28384| - gate/checkpoint;
> L28385| - direction;
> L28386| - timestamp;
> L28387| - access allowed/blocked;
> L28388| - online/offline;
> L28389| - weight em APPAWeb/TCP.
> L28422| - SEV;
> L28423| - appointments;
> L28424| - gate events;
> L28425| - checkpoints.
> L28429| - OCR reads;
> L28430| - RFID reads;
> L28431| - biometric decision;
> L28432| - barrier state.

### 5.4.36 Principais gaps → Integrações e Hardware atual (L28470 / L28472 / L28482)
> L28474| - SICS↔Ronda;
> L28475| - APPAWeb↔Ronda;
> L28476| - Ronda↔OCR;
> L28477| - Ronda↔RFID;
> L28478| - Ronda↔biometria;
> L28479| - Ronda↔Guardian;
> L28480| - Ronda↔FTP.
> L28484| - modelos atuais de controladores;
> L28485| - fabricantes atuais de leitores;
> L28486| - câmeras OCR;
> L28487| - antenas RFID;
> L28488| - cancelas;
> L28489| - torniquetes;
> L28490| - concentradoras;
> L28491| - servidores.

### 5.4.37 Workbook — resoluções (L28513, L28515) — established facts
> L28517| - `RESOLVIDO` Ronda Senior é sistema central atual de controle de acesso.
> L28522| - `RESOLVIDO` Senior é fabricante; MD Sistemas é integrador/suporte atual.
> L28525| - `RESOLVIDO` Totens: Mifare + TCP/IP + biometria.
> L28527| - `RESOLVIDO` Toledo 007/2017 = OCR de acesso.
> L28528| - `RESOLVIDO` regra atual de gate = RFID + OCR + biometria + autorização.
> L28529| - `RESOLVIDO` APPAWeb possui API de gate event TCP.
> L28530| - `RESOLVIDO` P16/GATE_TCP/GATE_BITREM aparecem como checkpoints/códigos operacionais.
> L28531| - `RESOLVIDO` API ViagensPendentes reconcilia missing checkpoints.
> L28532| - `RESOLVIDO` Ronda suporta web services.
> L28533| - `RESOLVIDO` Ronda suporta custom validation REST/SOAP.
> L28534| - `RESOLVIDO` payload de validação Senior pode conter card, vehicle card, plate, device, direction, name e last access.
> L28536| - `RESOLVIDO` Mifare adquirido/implantado.
> L28537| - `RESOLVIDO` 13 torniquetes e hand-keys biométricos documentados.
> L28538| - `RESOLVIDO` vigilância humana/ISPS é camada separada.

### 5.4.40 Deep dive adicional — correção da cadeia MD Sistemas / Senior (L28701)
> L28705| `Senior → Inteligate → MD Sistemas`.
> L28709| A **MD Sistemas já prestava “Manutenção Sênior” à APPA desde o Contrato 071/2020**, enquanto a Inteligate mantinha especificamente a **Solução de Totens** a partir de 2021.

### 5.4.42 O contrato 027/2026 revela migração de arquitetura Senior (L28789)
> L28793| - Ronda Senior;
> L28794| - módulos legados **ERP Senior**;
> L28795| - módulos legados **HCM Senior**;
> L28796| - migração/descontinuação;
> L28797| - ativação de novos equipamentos;
> L28798| - customizações e melhorias.
> L28809| Portanto, a arquitetura 2026 pode estar em transição.

### 5.4.45 Smart Card / Mifare em modo offline (L28879)
> L28888| Como APPA usa Mifare historicamente, existe **capability técnica** para operação resiliente do acesso mesmo com indisponibilidade parcial da rede.
> L28890| Não foi provado que os cartões APPA estejam configurados com todas essas funções de Smart Card; apenas Mifare e a capability do Ronda estão confirmados separadamente.

### 5.4.52 Pagamentos 2026 confirmam Inteligate ainda ativa (L29095)
> L29099| **Inteligate Tecnologias de Acesso**
> L29104| Isso confirma que a Inteligate ainda estava efetivamente prestando serviço em 2026, enquanto a MD já havia sido contratada emergencialmente para Ronda em outubro/2025.
> L29108| `Inteligate — Totens`
> L29109| \+
> L29110| `MD Sistemas — Ronda`.
> L29112| Isto reforça que “totem hardware/integration” e “Ronda software” são camadas contratuais distintas.

### 5.4.54 Camadas de segurança revisadas → Access device layer (L29157 / L29161)
> L29163| - Totens;
> L29164| - Digicon histórico;
> L29165| - leitores Mifare;
> L29166| - biometria;
> L29167| - RFID;
> L29168| - OCR;
> L29169| - cancelas;
> L29170| - torniquetes.

### 5.4.39 Referências — Canonical interface map (L28578)
> L28584| | SICS → eligibility | entrada | credencial/validade/perfil | APPA | **Confirmado funcional** |
> L28585| | APPAWeb/SEV → gate | entrada | autorização/SEV/vehicle event | doc Celepar | **Confirmado técnico em parte** |
> L28586| | Ronda Senior ↔ dispositivos | bidirecional | credencial, placa, reader, decisão, evento | produto + contrato | **Ronda central confirmado; topologia local parcial** |
> L28587| | OCR/RFID/biometria → decisão | entrada | plate/tag/driver | regulamento APPA | **Confirmado atual** |
> L28588| | Gate → APPA/UASP | saída | entrada/saída/bloqueio | processo de segurança | **Confirmado funcional** |

---

# 5.5 — BALANÇAS / AUTOMAÇÃO DE PESAGEM (entry/exit scale control)

### 5.5.1 Conclusão principal (L29362)
> L29400| - `vehicle identification`
> L29401| - `peripherals`
> L29402| - `Guardian`
> L29403| - `APPA operational systems`
> L29404| = subsistema de automação de pesagem.

### 5.5.2 Sistema atual — Guardian (L29408)
> L29416| - manutenções corretivas;
> L29417| - suporte técnico;
> L29418| - atualização;
> L29419| - configurações;
> L29420| - parametrizações especiais no **software Guardian**;
> L29421| - itens da Automação de Pesagem;
> L29422| - ambientes **Faixa e Silo**.

### 5.5.3 Contrato atual da camada física/periféricos (L29444)
> L29454| - cancelas;
> L29455| - semáforos;
> L29456| - câmeras OCR;
> L29457| - antenas RFID;
> L29458| - display;
> L29459| - equipamentos de comunicação em rede;
> L29460| - nobreaks;
> L29461| - impressoras de tickets.
> L29471| **Guardian**
> L29472| quanto
> L29473| **hardware/periféricos da solução de pesagem**

### 5.5.4 Separação contratual software vs. hardware (L29479 / L29493)
> L29497| - balanças;
> L29498| - OCR;
> L29499| - RFID;
> L29500| - semáforos;
> L29501| - cancelas;
> L29502| - rede;
> L29503| - tickets;
> L29504| - nobreaks.
> L29508| `Guardian application`
> L29509| ≠
> L29510| `field automation hardware`.

### 5.5.5 Histórico contratual da solução — Contrato 015/2021 (L29523)
> L29527| - manutenção preventiva/corretiva;
> L29528| - suporte nos periféricos;
> L29529| - solução de balanças rodoviárias e ferroviárias;
> L29530| - cancelas;
> L29531| - semáforos;
> L29532| - OCR;
> L29533| - RFID;
> L29534| - display;
> L29535| - rede;
> L29536| - nobreak;
> L29537| - impressora de tickets.

### 5.5.6 — Contrato 046/2023 (L29550)
> L29554| - manutenção corretiva;
> L29555| - suporte técnico;
> L29556| - atualizações de software;
> L29557| - itens da Automação de Pesagem.

### 5.5.8 Gate weighing vs. Guardian (L29615)
> L29623| `scale automation`
> L29624| → `Guardian`
> L29625| e
> L29626| `scale data ↔ APPAWeb`

### 5.5.9 Obrigatoriedade de pesagem (L29644) — entry/exit scale control
> L29648| > todos os veículos leves ou pesados devem ser pesados nas balanças de plataforma da APPA na entrada e saída, registrando diferenças de peso,
> L29659| Portanto, os tickets de pesagem são registros operacionais oficiais, não meramente apoio logístico.

### 5.5.10 Uso no controle ambiental (L29663)
> L29667| - veículo deve entrar vazio;
> L29668| - tara é estabelecida;
> L29669| - peso é novamente determinado;
> L29670| - tickets de entrada/saída fazem parte da comprovação documental.

### 5.5.11 Guardian — função do produto (L29692) — software attribution
> L29696| - gerenciamento de pesagem;
> L29697| - automação da pesagem de veículos;
> L29698| - controle de acesso de veículos;
> L29699| - integração de dados;
> L29700| - prevenção de fraudes;
> L29701| - monitoramento;
> L29702| - geração de tickets;
> L29703| - gestão de filas/pátio em versões atuais.
> L29707| - balança;
> L29708| - sensores;
> L29709| - cancelas;
> L29710| - semáforos;
> L29711| - displays;
> L29712| - RFID/UHF;
> L29713| - câmeras;
> L29714| - OCR.

### 5.5.12 Arquitetura Guardian publicada (L29722) — Estação de cadastramento / controle / Campo
> L29741| - aplicação Guardian;
> L29742| - leitor UHF de mesa.
> L29746| - aplicação de operação;
> L29747| - sinalização de erro OCR;
> L29748| - módulo controlador da automação;
> L29749| - terminal de pesagem.
> L29753| - câmeras/iluminadores OCR;
> L29754| - antena UHF;
> L29755| - semáforos;
> L29756| - display;
> L29757| - barreira OCR;
> L29758| - sensor de posicionamento;
> L29759| - cancelas.

### 5.5.14 Componentes Guardian identificados (L29786)
> L29790| - **Guardian Service**
> L29791| - **Guardian Configuração**
> L29792| - **Guardian LMP**
> L29793| - **TBROC** para OCR
> L29794| - aplicação Guardian
> L29795| - módulo controlador da automação
> L29796| - terminal de pesagem.

### 5.5.17 Interfaces de integração do Guardian (L29874)
> (Web Service de produto Guardian disponível de forma passiva/ativa SOAP ou REST; ver 5.5.50 e 5.5.52.)

### 5.5.18 Eventos e dados típicos do Guardian (L29899)
> L29903| - vehicle identity;
> L29904| - plate;
> L29905| - RFID/UHF;
> L29906| - driver/authorization linkage;
> L29907| - initial weight;
> L29908| - final weight;
> L29909| - tare;
> L29910| - gross;
> L29911| - net;
> L29912| - ticket;
> L29913| - timestamp;
> L29914| - scale/station;
> L29915| - direction;
> L29916| - position validation;
> L29917| - barrier state;
> L29918| - OCR result;
> L29919| - anomaly/fraud flag.

### 5.5.19 Dados diretamente comprovados no ecossistema APPA (L29925)
> L29929| - placa;
> L29930| - terminal;
> L29931| - ticket;
> L29932| - tara;
> L29933| - peso líquido;
> L29934| - timestamps de pesagem;
> L29935| - peso em evento de gate TCP/APPAWeb;
> L29936| - entrada/saída;
> L29937| - gate/checkpoint;
> L29938| - OCR;
> L29939| - RFID;
> L29940| - ticket impresso.

### 5.5.20 Infoger — consulta do realizado (L29955)
> L29965| - peso tara;
> L29966| - peso líquido;
> L29967| - data/hora das pesagens.
> L29969| Isto cria um consumidor/view pública/operacional de dados de pesagem.

### 5.5.21 Carga Online ↔ pesagem (L29983)
> L29987| - usa ferramentas de monitoramento;
> L29988| - identifica problemas/correções em sistemas de pesagem de terceiros.

### 5.5.22 APPAWeb ↔ peso em gate event (L30007)
> L30011| **`peso`**
> L30021| Portanto APPAWeb consegue armazenar/receber peso contextualizado por evento.
> L30025| Não se pode concluir automaticamente que todo `peso` venha do Guardian; a origem deve ser confirmada por checkpoint.

### 5.5.23 Pesagem e Receita / API Recintos (L30029)
> L30035| **pesagem-veiculos-cargas**
> L30037| Logo, o ecossistema APPAWeb atual possui uma camada de evento regulatório para pesagem.

### 5.5.24 Coordenação interna APPA de Pesos e Medidas (L30054)
> L30062| - balanças de fluxo;
> L30063| - balanças automáticas;
> L30064| - automação de pesagem;
> L30065| - ajuste/calibração.
> L30067| Isso confirma existência de competência técnica interna APPA dedicada a metrologia/pesagem.

### 5.5.30 Linha histórica da automação pública (L30176) — 2016 APPAWeb integration
> L30180| `balanças de acesso / automação inicial`
> L30181| → `integrações e modernização 2008–2013`
> L30182| → `4 novas balanças automáticas integradas ao APPAWeb em 2016`
> L30183| → `Toledo 015/2021`
> L30184| → `Toledo 046/2023`
> L30185| → `Toledo 011/2024 hardware`
> L30186| → `Toledo 045/2025 Guardian`
> L30187| → `aditivos até 2027`.

### 5.5.31 Procurement — concentração Toledo (L30193)
> L30195| Na camada de pesagem pública pesquisada, Toledo aparece repetidamente como:
> L30197| - fabricante;
> L30198| - integrador;
> L30199| - mantenedor;
> L30200| - fornecedor de software Guardian;
> L30201| - fornecedor/periféricos OCR/RFID;
> L30202| - suporte técnico.
> L30204| Não foi identificada nesta rodada concorrência tecnológica atual significativa no núcleo público de pesagem.

### 5.5.34 State machine funcional da pesagem (L30266) — gate automation
> L30270| `vehicle authorized`
> L30271| → `approaches scale`
> L30272| → `RFID/OCR identification`
> L30273| → `position validation`
> L30274| → `barrier/traffic-light control`
> L30275| → `weight stabilization`
> L30276| → `weight captured`
> L30277| → `ticket/event generated`
> L30278| → `vehicle released`
> L30279| → `second weighing when required`
> L30280| → `gross/tare/net calculated`
> L30281| → `APPA systems / regulatory reporting`.

### 5.5.46 API Recintos — pesagem é evento obrigatório em tempo real (L30796)
> L30804| O endpoint federal de pesagem é:
> L30806| `POST /recintos-ext/api/ext/pesagem-veiculos-cargas`
> L30810| - cada pesagem/repesagem é um evento independente;
> L30811| - pesagem rodoviária deve gerar evento;
> L30812| - balança de fluxo também pode gerar evento;
> L30813| - correias transportadoras podem ser tratadas de forma equivalente a dutos quando aplicável.

### 5.5.47 API Recintos — Release Paraná 2026 / tipoPesagem (L30823)
> L30831| **`tipoPesagem`**
> L30835| - `C` — Cavalo Mecânico ou Semirreboque, pesagem individual;
> L30836| - `CS` — Cavalo Mecânico + Semirreboque;
> L30837| - `CST` — Cavalo + Semirreboque + Contêiner;
> L30838| - `E` — Veículo de Carga Especial;
> L30839| - `O` — Outros, incluindo RTG e Dutos/Correias.

### 5.5.52 Guardian — métodos de negócio documentados (L30961) — software attribution
> L30971| `recepção motorista`
> L30972| → sistema cliente cadastra veículo/associa TAG
> L30973| → `CadastraTicketGuardian`
> L30974| → pesagem inicial
> L30975| → Guardian chama sistema cliente
> L30976| → carga/descarga
> L30977| → pesagem final
> L30978| → Guardian chama sistema cliente
> L30979| → `AcionaCancela`
> L30980| → `ManutencaoTicket`
> L30981| → ticket encerrado / TAG desassociada.
> L30985| - placa veículo;
> L30986| - placa carreta;
> L30987| - nota fiscal;
> L30988| - peso NF;
> L30989| - TAG;
> L30990| - número do ticket;
> L30991| - data/hora;
> L30992| - entrada/saída;
> L30993| - balança;
> L30994| - peso.

### 5.5.53 Guardian — arquitetura de automação física detalhada (L31000)
> L31004| A. computador Guardian / cadastramento TAG
> L31005| B. terminal de pesagem
> L31006| C. **MCA — Módulo de Controle da Automação**
> L31007| D. servidor de dados/aplicação
> L31008| E. antena UHF
> L31009| F. semáforo
> L31010| G. display
> L31011| H. câmera
> L31012| I. célula de carga digital
> L31013| J. cancela
> L31014| K. sensores de posicionamento.

### 5.5.57 OCR Guardian — arquitetura própria (L31104)
> L31106| No cenário Guardian atual, OCR pode incluir:
> L31108| - servidor exclusivo;
> L31109| - software **TBOCR**;
> L31110| - licença/hardkey;
> L31111| - câmeras;
> L31112| - iluminadores;
> L31113| - barreiras/sensores;
> L31114| - integração ao Guardian.

### 5.5.58 RFID/UHF Guardian (L31130) — tag access
> L31134| - antena UHF;
> L31135| - leitores transponder RFID;
> L31136| - associação TAG↔veículo;
> L31137| - caixas coletoras de TAG;
> L31138| - controle automático de acesso/pesagem.
> L31145| Mas a TAG usada no Guardian não deve ser automaticamente equiparada à TAG RFID do Ronda/Gate sem evidência de shared credential.

### 5.5.59 Controle de fila e pátio no produto Guardian (L31149) — queue/yard + agendamento
> L31153| - gestão de pátio/YMS;
> L31154| - agendamento;
> L31155| - filas;
> L31156| - chamada;
> L31157| - Guardian Fácil;
> L31158| - QR Code;
> L31159| - Cloud Prix.
> L31163| - Carga Online;
> L31164| - Pátio de Triagem;
> L31165| - APPAWeb.

### 5.5.61 Integração Guardian ↔ API Recintos — handoff provável (L31210)
> L31216| - Guardian como sistema de pesagem;
> L31217| - APPAWeb com event forwarding para API Recintos;
> L31218| - obrigação federal de transmitir pesagem em tempo real.
> L31230| - middleware Celepar;
> L31231| - acesso a banco;
> L31232| - sistema de controle intermediário;
> L31233| - publicação direta Guardian→serviço APPA.

### 5.5.43 Referências — canonical interface map (L30545)
> L30551| | Balanças/periféricos ↔ Guardian | bidirecional | peso, ticket, OCR, RFID, status | contrato Toledo + produto | **Confirmado** |
> L30552| | Balanças ↔ APPAWeb | integração | peso/controle de carga | APPA desde 2016 | **Confirmado institucionalmente** |
> L30553| | Guardian ↔ APPAWeb | provável atual | pesagem/evento | arquitetura funcional | **Não comprovado tecnicamente** |
> L30554| | Carga Online ↔ pesagem | funcional | monitoramento/correção | CELEPAR | **Confirmado funcional** |
> L30555| | Infoger ← pesagem | saída | tara, líquido, timestamps | serviço APPA | **Confirmado como view; backend não identificado** |
> L30556| | APPAWeb → API Recintos | saída federal | pesagem veículos/cargas | doc Celepar | **Confirmado técnico** |

### 5.5.37/5.5.40 — Classificação final → Confirmado atual (L30432)
> L30434| - Guardian instalado em Faixa e Silo.
> L30435| - Toledo é fornecedor atual.
> L30436| - Contrato 045/2025 vigente até 26/06/2027.
> L30437| - Solução de balanças rodoviárias e ferroviárias com OCR/RFID/periféricos.
> L30438| - Contrato 011/2024 vigente até 14/03/2027.
> L30440| - APPAWeb recebe peso em alguns eventos.
> L30441| - API Recintos possui evento de pesagem.

---

# 5.6 — OCR / LPR / PLACA

### 5.6.CEL-2026-B — APPAWeb ↔ OCR (L31474)
> L31476| O pacote CELEPAR 2026 inclui **OCR** entre os componentes do ambiente de segurança/controle de acesso integrado ao APPAWeb. Isso eleva a relação `APPAWeb ↔ OCR` de mera inferência operacional para **integração funcional documentada current**.

### 5.6.1 Objetivo (L31482)
> L31486| - OCR de gate/acesso;
> L31487| - OCR de pesagem;
> L31488| - OCR de scanner/inspeção;
> L31489| - OCR em terminais privados;
> L31490| - OCR como capability de fornecedor;
> L31491| - OCR integrado ao APPAWeb/SEV;
> L31492| - OCR integrado ao Guardian;
> L31493| - OCR histórico.

### 5.6.2 OCR/LPR no gate público (L31500) — license-plate capture
> L31504| - TAG RFID;
> L31505| - leitura OCR da placa;
> L31506| - biometria do condutor;
> L31507| - validação de credenciamento/autorização.

### 5.6.4 OCR dentro da solução de pesagem (L31538)
> L31542| - câmeras OCR;
> L31543| - balanças;
> L31544| - RFID;
> L31545| - cancelas;
> L31546| - semáforos;
> L31547| - displays;
> L31548| - rede;
> L31549| - impressoras de ticket.
> L31551| Portanto existe OCR ligado à automação de pesagem atual.

### 5.6.5 OCR no Guardian (L31558)
> L31560| Documentação Guardian mostra OCR como componente integrado ao sistema de pesagem, com:
> L31562| - câmeras;
> L31563| - iluminadores;
> L31564| - barreira/sensor;
> L31565| - software OCR;
> L31566| - serviço TBOCR;
> L31567| - sinalização de erro;
> L31568| - associação placa↔veículo/ticket.
> L31573| Deployment exato de TBOCR na APPA:
> L31574| **não comprovado localmente.**

### 5.6.6 OCR no APPAWeb/SEV (L31578)
> L31593| `OCR physical read`
> L31594| → `gate validation`
> L31595| → `APPAWeb/SEV event ecosystem`.
> L31597| A interface técnica OCR→APPAWeb ainda não está publicada.

### 5.6.9 OCR em balança vs. OCR de gate (L31632)
> L31636| - controle de acesso;
> L31637| - pesagem.

### 5.6.10 OCR em terminais privados (L31650)
> L31656| - TCP usa OCR no ecossistema de gate/terminal;
> L31657| - Ascensus declara OCR/RFID/CCTV em operação de veículos;
> L31658| - Marcon declara OCR/CCTV em retroárea;
> L31659| - inventários privados mostram OCR integrado a Guardian em instalações específicas.

### 5.6.11 Resultado da Passada 1 (L31666)
> L31670| 1. APPA gate OCR;
> L31671| 2. APPA weighing OCR;
> L31672| 3. Guardian OCR;
> L31673| 4. terminal/private OCR;
> L31674| 5. scanner/security imaging ecosystem.

### 5.6.14 TBOCR (L31725) — software attribution
> L31729| **TBOCR**
> L31731| como componente do ecossistema OCR Toledo.
> L31735| - servidor OCR;
> L31736| - software TBOCR;
> L31737| - hardkey/licença;
> L31738| - câmeras;
> L31739| - iluminadores;
> L31740| - conexão ao Guardian.

### 5.6.16 OCR/LPR no Ronda Senior (L31762)
> L31764| Ronda Senior possui capacidade de validar acesso com:
> L31775| Portanto, Ronda pode receber/use plate data em lógica de acesso.
> L31779| - OCR diretamente conectado ao Ronda;
> L31780| - middleware;
> L31781| - endpoint;
> L31782| - chamada específica.

### 5.6.17 Possíveis topologias OCR no gate (L31789)
> L31793| A)
> L31794| `Camera OCR → Ronda/Concentradora → decisão`
> L31796| B)
> L31797| `Camera OCR → APPAWeb/SEV → Ronda`
> L31799| C)
> L31800| `Camera OCR → sistema Toledo/field controller → APPAWeb`

### 5.6.19 OCR e Guardian ticket (L31826)
> L31828| No Guardian, OCR pode ser usado para:
> L31830| - identificar veículo;
> L31831| - validar placa;
> L31832| - associar pesagem ao ticket;
> L31833| - detectar inconsistência.
> L31837| `plate`
> L31838| ↔ `ticket`
> L31839| ↔ `RFID`
> L31840| ↔ `scale event`.

### 5.6.22 OCR em scanners de contêiner (L31883) — see 5.8; kept for OCR boundary
> (OCR de container/inspeção é domínio 5.8 e não se confunde com OCR de gate/balança — ver 5.6.38.)

### 5.6.24 Ascensus / RoRo (L31918)
> L31922| - OCR;
> L31923| - RFID;
> L31924| - CCTV;
> L31925| - software especializado de yard/ship.

### 5.6.25 Marcon (L31934)
> L31938| - CCTV;
> L31939| - OCR;
> L31940| - controles de retroárea.

### 5.6.32 OCR e Genetec (L32073)
> L32085| Não foi encontrada prova de integração Genetec↔OCR ou Genetec↔Ronda.

### 5.6.34 OCR e Guardian — maior certeza técnica (L32110)
> L32112| Guardian tem arquitetura documentada de OCR integrada.
> L32114| Portanto, no contexto de pesagem, a ligação:
> L32115| `OCR ↔ Guardian`
> L32116| é forte como capability.
> L32118| No contexto APPA atual, presença de OCR no contrato Toledo de pesagem torna essa arquitetura plausível, mas:
> L32119| **não foi encontrado documento de configuração local que nomeie TBOCR.**

### 5.6.38 Checagem de drift (L32190) — disambiguation
> L32194| 1. **Toledo OCR histórico ≠ Toledo OCR atual**
> L32196|    - preservado como histórico vs atual.
> L32197| 2. **Guardian OCR capability ≠ deployment TBOCR APPA**
> L32199|    - separado corretamente.
> L32200| 3. **Ronda accepts licensePlate ≠ Ronda receives OCR camera directly**
> L32202|    - separado corretamente.
> L32203| 4. **APPAWeb has plate ≠ APPAWeb owns OCR engine**
> L32205|    - separado corretamente.
> L32206| 5. **Genetec CCTV ≠ OCR**

### 5.6.41 Consistência de interfaces (L32254)
> L32258| - OCR→Ronda;
> L32259| - OCR→APPAWeb;
> L32260| - OCR→Genetec;
> L32261| - OCR→ApiRecintos;
> L32262| - OCR APPA→terminal.

### 5.6.37 Resultado da Passada 2 → Confirmado atual (L32164)
> L32166| - OCR faz parte do gate atual.
> L32167| - OCR faz parte do hardware/periféricos de pesagem atual.
> L32168| - Toledo é fornecedor atual do contexto de pesagem.
> L32169| - APPAWeb registra placa/gate/evento.
> L32170| - Ronda é núcleo de access control.
> L32171| - Guardian possui OCR como capability.

### 5.6.45 Referências — canonical interface map (L32336)
> L32342| | OCR gate → access decision | entrada | placa | regulamento APPA | **Confirmado funcional** |
> L32343| | OCR pesagem → Guardian | entrada | placa/ticket/vehicle | contrato + Toledo | **Fortemente suportado; TBOCR local não comprovado** |
> L32344| | OCR → Ronda | possível | `licensePlate` / vehicle | capability Ronda | **Não comprovado localmente** |
> L32345| | OCR → APPAWeb/SEV | possível/consequente | placa/gate/event | campos APPAWeb | **Handoff funcional; origem técnica não identificada** |
> L32346| | OCR terminal privado → sistema terminal | local | plate/read/event | TCP/Ascensus/Marcon | **Terminal-side** |

---

# 5.7 / 5.7A — PÁTIO DE TRIAGEM / REGULATOR-YARD ADMISSION

### 5.7.1 Escopo (L32441)
> L32447| - infraestrutura física;
> L32448| - controle de entrada/saída;
> L32449| - classificação vegetal;
> L32450| - fila/espera;
> L32451| - chamada para terminal;
> L32452| - Carga Online;
> L32453| - segurança;
> L32454| - pesagem;
> L32455| - gate;
> L32456| - iluminação/energia;
> L32457| - atores públicos;
> L32458| - ATEXP;
> L32459| - classificadora privada;
> L32460| - IDR-Paraná;
> L32461| - terminais exportadores.

### 5.7.5 Gate do Pátio (L32530)
> L32534| - guaritas informatizadas;
> L32535| - integração operacional ao Carga Online;
> L32536| - seis pistas na modernização histórica;
> L32537| - três guichês de entrada;
> L32538| - dois de saída;
> L32539| - uma pista reversível.
> L32542| **Confirmado histórico arquitetural.**

### 5.7.6 Fluxo operacional básico (L32548) — admission/triage chain
> L32552| `cadastro na origem`
> L32553| → `janela Carga Online`
> L32554| → `chegada ao Pátio`
> L32555| → `controle de entrada`
> L32556| → `ticket`
> L32557| → `amostragem`
> L32558| → `classificação`
> L32559| → `LIBERADA / REFUGADA`
> L32560| → `vaga/espera`
> L32561| → `chamada do terminal`
> L32562| → `saída do Pátio`
> L32563| → `terminal`
> L32564| → `descarga`.

### 5.7.9 Classificadora oficial (L32614)
> L32620| como classificadora oficial do Pátio, contratada pela ATEXP.
> L32624| - BV executa classificação;
> L32625| - IDR audita;
> L32626| - ATEXP gere/fiscaliza o serviço.

### 5.7.10 Mudança histórica da classificação (L32637)
> L32641| `Claspar`
> L32642| → `IDR-Paraná`
> L32643| → `ATEXP assume responsabilidade operacional da classificação em 2022`
> L32644| → `ATEXP contrata Bureau Veritas`
> L32645| → `IDR mantém papel de auditoria a partir de 2024`.

### 5.7.12 Resultado da Passada 1 (L32669)
> L32673| - Pátio é público/APPA;
> L32674| - Carga Online controla fluxo;
> L32675| - ATEXP opera a logística;
> L32676| - classificação privada é executada por empresa contratada;
> L32677| - IDR audita;
> L32678| - gate/classificação/chamada/terminal formam uma única cadeia operacional;
> L32679| - não há evidência de YMS independente.
> L32683| - sistema interno ATEXP;
> L32684| - software da BV;
> L32685| - interface classificação→Carga Online;
> L32686| - state machine completa;
> L32687| - distribuição de vagas;
> L32688| - chamada de caminhões;
> L32689| - integração com gate/balança;
> L32690| - hardware atual.

### 5.7.14 Portaria 163/2025 — reclassificação e contestação (L32708)
> L32721| - realiza amostragem/classificação;
> L32722| - pode ter sua atividade auditada pelo IDR;
> L32723| - pode ter resultado contestado segundo procedimento formal.

### 5.7.15 Procedimento SGI 029 (L32734)
> L32736| O PO-APPA-SGI-029 estabelece que a classificação vegetal:
> L32738| - ocorre em instalação física própria no Pátio;
> L32739| - possui requisitos de SSMA;
> L32740| - área de amostragem deve ser controlada/sinalizada;
> L32741| - ATEXP e/ou sua classificadora contratada mantém organização do fluxo;
> L32742| - envolve galpão, pistas internas e posicionamento de caminhões.

### 5.7.17 Resultado da classificação entra no Carga Online (L32769)
> L32782| `classificadora/IDR process`
> L32783| → `Carga Online`

### 5.7.26 Sistema interno da ATEXP (L32958)
> L32969| Entretanto:
> L32970| **não há evidência de que OTK Web seja o sistema operacional de dispatch/classificação do Pátio.**

### 5.7.27 Não foi identificado YMS separado (L32981)
> L32985| - YMS;
> L32986| - yard management;
> L32987| - Pátio software;
> L32988| - ATEXP software;
> L32989| - dispatch;
> L32990| - calling system;
> L32991| - classification system;

### 5.7.37 Sistemas do Pátio — inventário consolidado → Confirmado deployment (L33179 / L33181)
> L33183| - Carga Online;
> L33184| - gate informatizado;
> L33185| - classificação operational workflow;
> L33186| - CCTV em classificação;
> L33187| - iluminação automatizada/supervisionada;
> L33188| - sistemas de segurança/acesso adjacentes.

### 5.7.38 Integrações confirmadas → Não confirmado (L33205 / L33224)
> L33226| - BV→COL protocol;
> L33227| - ATEXP→COL;
> L33228| - COL→gate;
> L33229| - COL→Guardian;
> L33230| - COL→Ronda;
> L33231| - COL→lighting;
> L33232| - CCTV integration.

### 5.7.51 Referências — canonical interface map (L33495)
> L33501| | Carga Online → Pátio | planejamento | janela, terminal, quota, carga | APPA/IDR | **Confirmado** |
> L33502| | Gate/Pátio → Carga Online | evento/status | chegada/admissão/processo | processo APPA | **Confirmado funcional; API exata não publicada** |
> L33503| | Classificadora/Controladora → Carga Online | entrada | resultado, laudo, autorização | Portaria 163/2025 | **Confirmado funcional** |
> L33504| | IDR ↔ classificação | auditoria | qualidade/reclassificação | IDR/APPA | **Confirmado** |
> L33505| | Terminal → Pátio | capacidade/chamada | ready/call/receiving capacity | operação | **Confirmado funcional; interface não identificada** |
> L33506| | Pátio ↔ Guardian/Ronda | passagem/pesagem/acesso | gate, weight, identity | sistemas adjacentes | **Boundary funcional; integração técnica parcial** |

### 5.7A.1 Correção importante do instrumento APPA↔ATEXP (L33644)
> L33652| - o acordo original cobre operação, limpeza e manutenção do COREX;
> L33653| - o **1º Termo Aditivo** transferiu à ATEXP a responsabilidade pela **classificação prévia das cargas de granéis sólidos de origem vegetal no Pátio de Triagem da APPA**.
> L33659| `Acordo 069/2020`
> L33660| → `1º TA: responsabilidade de classificação no Pátio passa à ATEXP`
> L33661| → `Acordo 062 atual: cooperação APPA↔ATEXP continua abrangendo qualidade/classificação no Pátio`.

### 5.7A.2 Fluxo de classificação — regras concretas da Portaria 163/2025 (L33668) — regulator-yard admission
> L33674| - os resultados das análises devem ser inseridos no **Carga Online**;
> L33675| - a inserção é feita pela **Controladora contratada**, credenciada pela Portos do Paraná;
> L33676| - a Controladora confere os registros de qualidade;
> L33677| - a Controladora autoriza a descarga nos terminais Leste/Oeste e terminais exportadores de granéis sólidos;
> L33678| - o IDR-Paraná audita o trabalho;
> L33679| - reclassificação pode ter classificador designado pelo cliente/exportador;
> L33680| - classificadores externos devem ser formalmente nomeados à ATEXP.

### 5.7A.9 OTK Web — fechamento definitivo (L33834)
> (OTK Web confirmado na ATEXP para gestão empresarial/compras; **não** suportado como YMS ou sistema de dispatch/classificação do Pátio — ver 5.7.26 e 5.7.27.)

---

## End of compact evidence index

Extraction notes:
- All passages are verbatim from the source; only the leading `L<lineno>| ` label is added to carry the original line number.
- Blocks are grouped by the dossier's own section (5.4, 5.5, 5.6, 5.7/5.7A) which corresponds to the eight target functions.
- Bracketed short notes `(…)` added by this index are editorial signposts to keep adjacent evidence readable; the quoted source text itself is untouched.
- Where a block was edited into a compact form (e.g. skipping an interleaved PortX-proposed canonical model), the still-relevant established fact is retained.
