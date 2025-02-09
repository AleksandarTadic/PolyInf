/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     9/18/2023 2:21:18 PM                         */
/*==============================================================*/


drop table if exists AKTIVNOSTI_U_ETAPI;

drop table if exists DODELJENA;

drop table if exists DOMEN_ZAHTEVA;

drop table if exists DRZAVA;

drop table if exists ELEMENT_ZNANJA;

drop table if exists ETAPE_U_PROJEKTU;

drop table if exists ISPORUCENO;

drop table if exists KATALOG_AKTIVNOSTI;

drop table if exists KLASIFIKATOR;

drop table if exists KOMPETENCIJE_ZA_AKTIVNOST;

drop table if exists KONFIGURACIJA;

drop table if exists KORPUS_ZNANJA;

drop table if exists KO_SE_PITA;

drop table if exists LJUDSKI_RESURSI;

drop table if exists MAPA_KOMPETENCIJA;

drop table if exists NASELJENO_MESTO;

drop table if exists OBLAST_ZNANJA;

drop table if exists ORGANIZACIONE_JEDINICE;

drop table if exists PLASMAN_KONFIGURACIJE;

drop table if exists PODRZANE_U;

drop table if exists POSLOVNI_PARTNERI;

drop table if exists POSLOVNI_SUBJEKAT;

drop table if exists POTREBNE_KOMPETENCIJE;

drop table if exists POVEZANI_KORPUSI_ZNANJA;

drop table if exists PRIORITET;

drop table if exists PROFIL_KOMPETENCIJA;

drop table if exists PROIZVODI_U_ETAPI;

drop table if exists PROJEKAT_REALIZACIJE_SOFTVERA;

drop table if exists PROJEKTNI_ZAHTEVI;

drop table if exists RADNA_MESTA;

drop table if exists RASPORED_PO_JEDINICAMA;

drop table if exists REGISTAR_DELATNOSTI;

drop table if exists REGISTROVAN_ZA_DELATNOST;

drop table if exists SASTAV;

drop table if exists SASTAV__U_VERZIJI;

drop table if exists SEGMENT_ZNANJA;

drop table if exists SOFTVERSKI_PROCES;

drop table if exists SOFTVERSKI_PROIZVOD;

drop table if exists STATUS_ZAHTEVA;

drop table if exists STA_JE_PREDMET_PROJEKTA;

drop table if exists STA_SE_PREDAJE_U_AKTIVNOSTI;

drop table if exists STRUKTURA_AKTIVNOSTI;

drop table if exists STRUKTURA_PROCESA;

drop table if exists TIP_PROJEKTA;

drop table if exists UGOVORI_O_ANGAZOVANJU;

drop table if exists ULOGE;

drop table if exists UNUTRASNJA_ORGANIZACIJA;

drop table if exists VERZIJA;

drop table if exists VEZANE_DISCIPLINE;

drop table if exists VEZANI_ELEMENTI;

drop table if exists VEZANI_SEGMENTI;

drop table if exists VRSTA_ANGAZOVANJA;

drop table if exists VRSTA_PARTNERSTVA;

drop table if exists ZAINTERESOVANE_STRANE;

/*==============================================================*/
/* Table: AKTIVNOSTI_U_ETAPI                                    */
/*==============================================================*/
create table AKTIVNOSTI_U_ETAPI
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   TIPP_D               char(1) not null,
   PROJ_ID              int not null,
   PROJ_REVIZIJA        int not null,
   ETAPA_ID             int not null,
   AKT_OZNAKA           char(2) not null,
   AKTET_RBR            smallint not null,
   AKTET_PLANSKI_POCETAK date not null,
   AKTET_PLANSKI_ZAVRSETAK date not null,
   AKTET_STVARNI_POCETAK date,
   AKTET_STVARNI_ZAVRSETAK date,
   primary key (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID, AKT_OZNAKA, AKTET_RBR)
);

/*==============================================================*/
/* Table: DODELJENA                                             */
/*==============================================================*/
create table DODELJENA
(
   AKT_DR_OZNAKA        char(4) not null,
   AKT_PS_ID            int not null,
   TIPP_D               char(1) not null,
   PROJ_ID              int not null,
   PROJ_REVIZIJA        int not null,
   ETAPA_ID             int not null,
   AKT_OZNAKA           char(2) not null,
   AKTET_RBR            smallint not null,
   DOD_BROJ_DODELE      smallint not null,
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   LJ_ID                bigint not null,
   DOD_OD               date not null,
   DOD_DO               date,
   primary key (AKT_DR_OZNAKA, AKT_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID, AKT_OZNAKA, AKTET_RBR, DOD_BROJ_DODELE)
);

/*==============================================================*/
/* Table: DOMEN_ZAHTEVA                                         */
/*==============================================================*/
create table DOMEN_ZAHTEVA
(
   DZ_ID                smallint not null,
   DZ_NAZIV             varchar(80) not null,
   primary key (DZ_ID)
);

/*==============================================================*/
/* Table: DRZAVA                                                */
/*==============================================================*/
create table DRZAVA
(
   DR_OZNAKA            char(4) not null,
   DR_NAZIV             varchar(60) not null,
   primary key (DR_OZNAKA)
);

/*==============================================================*/
/* Table: ELEMENT_ZNANJA                                        */
/*==============================================================*/
create table ELEMENT_ZNANJA
(
   KZ_IDENT             int not null,
   KA_OBLAST            char(2) not null,
   SO_OZNAKA            numeric(2,0) not null,
   EZ_OZNAKA            numeric(2,0) not null,
   EZ_NAZIV             varchar(160) not null,
   EZ_OPIS              varchar(1024),
   primary key (KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA)
);

/*==============================================================*/
/* Table: ETAPE_U_PROJEKTU                                      */
/*==============================================================*/
create table ETAPE_U_PROJEKTU
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   TIPP_D               char(1) not null,
   PROJ_ID              int not null,
   PROJ_REVIZIJA        int not null,
   ETAPA_ID             int not null,
   ETAP_PLANIRANI_POCETAK date not null,
   ETAP_PLANIRANI_ZAVRSETAK date not null,
   ETAP_STVARNI_POCETAK date,
   ETAP_STVARNI_ZAVRSETAK date,
   primary key (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID)
);

/*==============================================================*/
/* Table: ISPORUCENO                                            */
/*==============================================================*/
create table ISPORUCENO
(
   DR_OZNAKA            char(4) not null,
   PLA_PS_ID            int not null,
   PLA_GODINA           numeric(4,0) not null,
   PLA_BROJ_PLASMANA    int not null,
   PPL_RBR              numeric(4,0) not null,
   SOF_DR_OZNAKA        char(4) not null,
   POS_PS_ID            int not null,
   SPR_KATBR            char(10) not null,
   SPR_TIP              char(1) not null,
   VER_OZNAKA           int not null,
   KONF_ID              int not null,
   POS_DR_OZNAKA        char(4) not null,
   PS_ID                int not null,
   PPL_PLANIRANO        date,
   PPL_REALIZOVANO      date,
   primary key (DR_OZNAKA, PLA_PS_ID, PLA_GODINA, PLA_BROJ_PLASMANA, PPL_RBR)
);

/*==============================================================*/
/* Table: KATALOG_AKTIVNOSTI                                    */
/*==============================================================*/
create table KATALOG_AKTIVNOSTI
(
   AKT_OZNAKA           char(2) not null,
   AKT_NAZIV            varchar(240) not null,
   primary key (AKT_OZNAKA)
);

/*==============================================================*/
/* Table: KLASIFIKATOR                                          */
/*==============================================================*/
create table KLASIFIKATOR
(
   KAT_ID               char(1) not null,
   KAT_NAZIV            varchar(60) not null,
   primary key (KAT_ID)
);

/*==============================================================*/
/* Table: KOMPETENCIJE_ZA_AKTIVNOST                             */
/*==============================================================*/
create table KOMPETENCIJE_ZA_AKTIVNOST
(
   AKT_OZNAKA           char(2) not null,
   AKT_KOMP             smallint not null,
   KZ_IDENT             int not null,
   KA_OBLAST            char(2) not null,
   SO_OZNAKA            numeric(2,0) not null,
   EZ_OZNAKA            numeric(2,0) not null,
   AKT_NIVO_MIN         numeric(3,2) not null,
   AKT_NIVO_MAX         numeric(3,2) not null,
   primary key (AKT_OZNAKA, AKT_KOMP)
);

/*==============================================================*/
/* Table: KONFIGURACIJA                                         */
/*==============================================================*/
create table KONFIGURACIJA
(
   SOF_DR_OZNAKA        char(4) not null,
   POS_PS_ID            int not null,
   SPR_KATBR            char(10) not null,
   SPR_TIP              char(1) not null,
   VER_OZNAKA           int not null,
   KONF_ID              int not null,
   KONF_NAZIV           varchar(240) not null,
   KONF_ISPOR           bool not null,
   primary key (SOF_DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA, KONF_ID)
);

/*==============================================================*/
/* Table: KORPUS_ZNANJA                                         */
/*==============================================================*/
create table KORPUS_ZNANJA
(
   KZ_IDENT             int not null,
   KZ_NAZIV             varchar(180) not null,
   KZ_SKRACENICA        varchar(10),
   KZ_WEB_LINK          varchar(120),
   KZ_OPIS              varchar(1024),
   primary key (KZ_IDENT)
);

/*==============================================================*/
/* Table: KO_SE_PITA                                            */
/*==============================================================*/
create table KO_SE_PITA
(
   PRO_DR_OZNAKA        char(4) not null,
   PRO_PS_ID            int not null,
   TIPP_D               char(1) not null,
   PROJ_ID              int not null,
   PROJ_REVIZIJA        int not null,
   DZ_ID                smallint not null,
   ZAHTEV_ID            int not null,
   ZAHTEV_VERZIJA       smallint not null,
   ZAIN_ID              int not null,
   ZAIN_TIP             char(1) not null default 'K',
   ULO_OZNAKA           char(3) not null,
   KOM_KOMENTAR         varchar(600),
   primary key (PRO_DR_OZNAKA, PRO_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, DZ_ID, ZAHTEV_ID, ZAHTEV_VERZIJA, ZAIN_ID, ZAIN_TIP, ULO_OZNAKA)
);

/*==============================================================*/
/* Table: LJUDSKI_RESURSI                                       */
/*==============================================================*/
create table LJUDSKI_RESURSI
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   LJ_ID                bigint not null,
   LJ_PREZIME           varchar(12) not null,
   LJ_IME_RODITELJA     varchar(12),
   LJ_IME               varchar(12) not null,
   primary key (DR_OZNAKA, PS_ID, LJ_ID)
);

/*==============================================================*/
/* Table: MAPA_KOMPETENCIJA                                     */
/*==============================================================*/
create table MAPA_KOMPETENCIJA
(
   AKT_DR_OZNAKA        char(4) not null,
   AKT_PS_ID            int not null,
   TIPP_D               char(1) not null,
   PROJ_ID              int not null,
   PROJ_REVIZIJA        int not null,
   ETAPA_ID             int not null,
   AKT_OZNAKA           char(2) not null,
   AKTET_RBR            smallint not null,
   DOD_BROJ_DODELE      smallint not null,
   KZ_IDENT             int not null,
   KA_OBLAST            char(2) not null,
   SO_OZNAKA            numeric(2,0) not null,
   EZ_OZNAKA            numeric(2,0) not null,
   MAP_VREDNOST         numeric(3,2) not null,
   primary key (AKT_DR_OZNAKA, AKT_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID, AKT_OZNAKA, AKTET_RBR, DOD_BROJ_DODELE)
);

/*==============================================================*/
/* Table: NASELJENO_MESTO                                       */
/*==============================================================*/
create table NASELJENO_MESTO
(
   DR_OZNAKA            char(4) not null,
   NM_ID                int not null,
   NM_NAZIV             varchar(40),
   primary key (DR_OZNAKA, NM_ID)
);

/*==============================================================*/
/* Table: OBLAST_ZNANJA                                         */
/*==============================================================*/
create table OBLAST_ZNANJA
(
   KZ_IDENT             int not null,
   KA_OBLAST            char(2) not null,
   KA_NAZIV             varchar(180) not null,
   KA_OPIS              varchar(1024),
   primary key (KZ_IDENT, KA_OBLAST)
);

/*==============================================================*/
/* Table: ORGANIZACIONE_JEDINICE                                */
/*==============================================================*/
create table ORGANIZACIONE_JEDINICE
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   OJ_ID                int not null,
   OJ_NAZIV             varchar(120) not null,
   NAS_DR_OZNAKA        char(4),
   NM_ID                int,
   OJ_ADRESA            varchar(60) not null,
   OJ_PRAVNO_LICE       bool default 0,
   primary key (DR_OZNAKA, PS_ID, OJ_ID)
);

/*==============================================================*/
/* Table: PLASMAN_KONFIGURACIJE                                 */
/*==============================================================*/
create table PLASMAN_KONFIGURACIJE
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   PLA_GODINA           numeric(4,0) not null,
   PLA_BROJ_PLASMANA    int not null,
   POS_DR_OZNAKA        char(4) not null,
   POS_PS_ID            int not null,
   PLA_DATUM_UG         date not null,
   primary key (DR_OZNAKA, PS_ID, PLA_GODINA, PLA_BROJ_PLASMANA)
);

/*==============================================================*/
/* Table: PODRZANE_U                                            */
/*==============================================================*/
create table PODRZANE_U
(
   ORG_DR_OZNAKA        char(4) not null,
   PS_ID                int not null,
   OJ_ID                int not null,
   REG_DR_OZNAKA        char(4) not null,
   DR_OZNAKA            char(4) not null,
   REGD_ID              int not null,
   REG_DATUM_REG        date not null,
   UOJ_OD               date not null,
   UOJ_DO               date,
   primary key (REG_DR_OZNAKA, ORG_DR_OZNAKA, DR_OZNAKA, REGD_ID, PS_ID, OJ_ID, REG_DATUM_REG, UOJ_OD)
);

/*==============================================================*/
/* Table: POSLOVNI_PARTNERI                                     */
/*==============================================================*/
create table POSLOVNI_PARTNERI
(
   DR_OZNAKA            char(4) not null,
   POS_PS_ID            int not null,
   POS_DR_OZNAKA        char(4) not null,
   PS_ID                int not null,
   VP_ID                smallint not null,
   PAR_OD               date not null,
   PAR_DO               date,
   primary key (POS_DR_OZNAKA, DR_OZNAKA, POS_PS_ID, VP_ID, PS_ID, PAR_OD)
);

/*==============================================================*/
/* Table: POSLOVNI_SUBJEKAT                                     */
/*==============================================================*/
create table POSLOVNI_SUBJEKAT
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   PS_NAZIV             varchar(120) not null,
   NM_ID                int not null,
   PS_ADRESA            varchar(60) not null,
   PS_WWW               varchar(60),
   POS_DR_OZNAKA        char(4),
   POS_PS_ID            int,
   primary key (DR_OZNAKA, PS_ID)
);

/*==============================================================*/
/* Table: POTREBNE_KOMPETENCIJE                                 */
/*==============================================================*/
create table POTREBNE_KOMPETENCIJE
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   RM_ID                int not null,
   KZ_IDENT             int not null,
   KA_OBLAST            char(2) not null,
   SO_OZNAKA            numeric(2,0) not null,
   EZ_OZNAKA            numeric(2,0) not null,
   POTR_MININIVO        numeric(3,2) not null,
   POTR_MAKSNIVO        numeric(3,2) not null,
   primary key (DR_OZNAKA, PS_ID, RM_ID, KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA)
);

/*==============================================================*/
/* Table: POVEZANI_KORPUSI_ZNANJA                               */
/*==============================================================*/
create table POVEZANI_KORPUSI_ZNANJA
(
   KZ_IDENT             int not null,
   KOR_KZ_IDENT         int not null,
   primary key (KZ_IDENT, KOR_KZ_IDENT)
);

/*==============================================================*/
/* Table: PRIORITET                                             */
/*==============================================================*/
create table PRIORITET
(
   PRIOR_ID             char(1) not null,
   PRIOR_NAZIV          varchar(40) not null,
   primary key (PRIOR_ID)
);

/*==============================================================*/
/* Table: PROFIL_KOMPETENCIJA                                   */
/*==============================================================*/
create table PROFIL_KOMPETENCIJA
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   LJ_ID                bigint not null,
   KOMP_RBR             smallint not null,
   KZ_IDENT             int not null,
   KA_OBLAST            char(2) not null,
   SO_OZNAKA            numeric(2,0) not null,
   EZ_OZNAKA            numeric(2,0) not null,
   KOMP_DAT_VRED        date not null,
   KOMP_OCENA           numeric(3,2) not null,
   LJU_LJ_ID            bigint not null,
   KOMP_CURRENT         bool not null default 0,
   primary key (DR_OZNAKA, PS_ID, LJ_ID, KOMP_RBR)
);

/*==============================================================*/
/* Table: PROIZVODI_U_ETAPI                                     */
/*==============================================================*/
create table PROIZVODI_U_ETAPI
(
   ETA_DR_OZNAKA        char(4) not null,
   ETA_PS_ID            int not null,
   TIPP_D               char(1) not null,
   PROJ_ID              int not null,
   PROJ_REVIZIJA        int not null,
   ETAPA_ID             int not null,
   STA_SPR_KATBR        char(10) not null,
   STA_SPR_TIP          char(1) not null,
   STA_VER_OZNAKA       int not null,
   primary key (ETA_DR_OZNAKA, ETA_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID, STA_SPR_KATBR, STA_SPR_TIP, STA_VER_OZNAKA)
);

/*==============================================================*/
/* Table: PROJEKAT_REALIZACIJE_SOFTVERA                         */
/*==============================================================*/
create table PROJEKAT_REALIZACIJE_SOFTVERA
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   TIPP_D               char(1) not null,
   PROJ_ID              int not null,
   PROJ_REVIZIJA        int not null,
   PROJ_NAZIV           varchar(240) not null,
   PROJ_DATPOKR         date not null,
   PROJ_DATOKON         date not null,
   PROJ_STVARNI_POCETAK date,
   PROJ_STVARNI_ZAVRSETAK date,
   ID_PROCESA           smallint not null,
   primary key (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA)
);

/*==============================================================*/
/* Table: PROJEKTNI_ZAHTEVI                                     */
/*==============================================================*/
create table PROJEKTNI_ZAHTEVI
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   TIPP_D               char(1) not null,
   PROJ_ID              int not null,
   PROJ_REVIZIJA        int not null,
   DZ_ID                smallint not null,
   ZAHTEV_ID            int not null,
   ZAHTEV_VERZIJA       smallint not null,
   ZAHTEV_NAZIV         varchar(120) not null,
   ZAHTEV_OPIS          varchar(7000),
   KAT_ID               char(1),
   PRIOR_ID             char(1),
   ISTAT_ID             char(1),
   primary key (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, DZ_ID, ZAHTEV_ID, ZAHTEV_VERZIJA)
);

/*==============================================================*/
/* Table: RADNA_MESTA                                           */
/*==============================================================*/
create table RADNA_MESTA
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   RM_ID                int not null,
   RM_NAZIV             varchar(80) not null,
   RM_NORM              numeric(4,0) not null default 1,
   primary key (DR_OZNAKA, PS_ID, RM_ID)
);

/*==============================================================*/
/* Table: RASPORED_PO_JEDINICAMA                                */
/*==============================================================*/
create table RASPORED_PO_JEDINICAMA
(
   ORG_DR_OZNAKA        char(4) not null,
   PS_ID                int not null,
   OJ_ID                int not null,
   DR_OZNAKA            char(4) not null,
   RM_ID                int not null,
   OJ_NORM              numeric(4,0) not null,
   primary key (ORG_DR_OZNAKA, DR_OZNAKA, PS_ID, OJ_ID, RM_ID)
);

/*==============================================================*/
/* Table: REGISTAR_DELATNOSTI                                   */
/*==============================================================*/
create table REGISTAR_DELATNOSTI
(
   DR_OZNAKA            char(4) not null,
   REGD_ID              int not null,
   REGD_NAZIV           varchar(120) not null,
   primary key (DR_OZNAKA, REGD_ID)
);

/*==============================================================*/
/* Table: REGISTROVAN_ZA_DELATNOST                              */
/*==============================================================*/
create table REGISTROVAN_ZA_DELATNOST
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   REGD_ID              int not null,
   REG_DATUM_REG        date not null,
   REG_DO_KADA          date,
   primary key (DR_OZNAKA, PS_ID, REGD_ID, REG_DATUM_REG)
);

/*==============================================================*/
/* Table: SASTAV                                                */
/*==============================================================*/
create table SASTAV
(
   SOF_DR_OZNAKA        char(4) not null,
   POS_PS_ID            int not null,
   KON_SPR_KATBR        char(10) not null,
   KON_SPR_TIP          char(1) not null,
   KON_VER_OZNAKA       int not null,
   KONF_ID              int not null,
   SASTAV_RBR           smallint not null,
   VER_SOF_DR_OZNAKA    char(4) not null,
   VER_POS_PS_ID        int not null,
   SPR_KATBR            char(10) not null,
   SPR_TIP              char(1) not null,
   VER_OZNAKA           int not null,
   primary key (SOF_DR_OZNAKA, POS_PS_ID, KON_SPR_KATBR, KON_SPR_TIP, KON_VER_OZNAKA, KONF_ID, SASTAV_RBR)
);

/*==============================================================*/
/* Table: SASTAV__U_VERZIJI                                     */
/*==============================================================*/
create table SASTAV__U_VERZIJI
(
   STR_AKT_OZNAKA       char(2) not null,
   AKT_VERZIJA          smallint not null,
   AKT_OZNAKA           char(2) not null,
   primary key (STR_AKT_OZNAKA, AKT_OZNAKA, AKT_VERZIJA)
);

/*==============================================================*/
/* Table: SEGMENT_ZNANJA                                        */
/*==============================================================*/
create table SEGMENT_ZNANJA
(
   KZ_IDENT             int not null,
   KA_OBLAST            char(2) not null,
   SO_OZNAKA            numeric(2,0) not null,
   SO_NAZIV             varchar(160) not null,
   SO_OPIS              varchar(1024),
   primary key (KZ_IDENT, KA_OBLAST, SO_OZNAKA)
);

/*==============================================================*/
/* Table: SOFTVERSKI_PROCES                                     */
/*==============================================================*/
create table SOFTVERSKI_PROCES
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   ID_PROCESA           smallint not null,
   PROC_NAZIV           varchar(120) not null,
   primary key (DR_OZNAKA, PS_ID, ID_PROCESA)
);

/*==============================================================*/
/* Table: SOFTVERSKI_PROIZVOD                                   */
/*==============================================================*/
create table SOFTVERSKI_PROIZVOD
(
   DR_OZNAKA            char(4) not null,
   POS_PS_ID            int not null,
   SPR_KATBR            char(10) not null,
   SPR_TIP              char(1) not null,
   SPR_NAZIV            varchar(240) not null,
   DATUM_KATALOGIZIRANJA date,
   DATUM_OBUSTAVLJANJA  date,
   POS_DR_OZNAKA        char(4),
   PS_ID                int,
   SPR_STATUS           char(1) not null default 'R',
   primary key (DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP)
);

/*==============================================================*/
/* Table: STATUS_ZAHTEVA                                        */
/*==============================================================*/
create table STATUS_ZAHTEVA
(
   ISTAT_ID             char(1) not null,
   ISTAT_NAZIV          varchar(40) not null,
   primary key (ISTAT_ID)
);

/*==============================================================*/
/* Table: STA_JE_PREDMET_PROJEKTA                               */
/*==============================================================*/
create table STA_JE_PREDMET_PROJEKTA
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   TIPP_D               char(1) not null,
   PROJ_ID              int not null,
   PROJ_REVIZIJA        int not null,
   SPR_KATBR            char(10) not null,
   SPR_TIP              char(1) not null,
   VER_OZNAKA           int not null,
   primary key (SPR_KATBR, SPR_TIP, DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, VER_OZNAKA)
);

/*==============================================================*/
/* Table: STA_SE_PREDAJE_U_AKTIVNOSTI                           */
/*==============================================================*/
create table STA_SE_PREDAJE_U_AKTIVNOSTI
(
   AKT_DR_OZNAKA        char(4) not null,
   AKT_PS_ID            int not null,
   AKT_TIPP_D           char(1) not null,
   AKT_PROJ_ID          int not null,
   AKT_PROJ_REVIZIJA    int not null,
   AKT_ETAPA_ID2        int not null,
   AKT_AKT_OZNAKA       char(2) not null,
   AKT_AKTET_RBR        smallint not null,
   PRO_STA_SPR_KATBR    char(10) not null,
   PRO_STA_SPR_TIP      char(1) not null,
   STA_VER_OZNAKA       int not null,
   primary key (AKT_DR_OZNAKA, AKT_PS_ID, AKT_TIPP_D, AKT_PROJ_ID, AKT_PROJ_REVIZIJA, AKT_ETAPA_ID2, AKT_AKT_OZNAKA, AKT_AKTET_RBR, PRO_STA_SPR_KATBR, PRO_STA_SPR_TIP, STA_VER_OZNAKA)
);

/*==============================================================*/
/* Table: STRUKTURA_AKTIVNOSTI                                  */
/*==============================================================*/
create table STRUKTURA_AKTIVNOSTI
(
   AKT_OZNAKA           char(2) not null,
   AKT_VERZIJA          smallint not null,
   AKT_DATFORM          date not null,
   primary key (AKT_OZNAKA, AKT_VERZIJA)
);

/*==============================================================*/
/* Table: STRUKTURA_PROCESA                                     */
/*==============================================================*/
create table STRUKTURA_PROCESA
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   ID_PROCESA           smallint not null,
   AKT_OZNAKA           char(2) not null,
   AKT_VERZIJA          smallint not null,
   primary key (DR_OZNAKA, PS_ID, AKT_OZNAKA, ID_PROCESA, AKT_VERZIJA)
);

/*==============================================================*/
/* Table: TIP_PROJEKTA                                          */
/*==============================================================*/
create table TIP_PROJEKTA
(
   TIPP_D               char(1) not null,
   TIPP_NAZIV           varchar(60) not null,
   primary key (TIPP_D)
);

/*==============================================================*/
/* Table: UGOVORI_O_ANGAZOVANJU                                 */
/*==============================================================*/
create table UGOVORI_O_ANGAZOVANJU
(
   POS_DR_OZNAKA        char(4) not null,
   PS_ID                int not null,
   EA_GODINA            numeric(4,0) not null,
   EA_EBROJ             numeric(4,0) not null,
   LJ_ID                bigint not null,
   VA_OZNAKA            char(2) not null,
   EA_DATUM_UGOVORA     date not null,
   EA_PERIOD_OD         date not null,
   EA_PERIOD_DO         date,
   OJ_ID                int not null,
   RM_ID                int not null,
   LJU_LJ_ID            bigint not null,
   primary key (POS_DR_OZNAKA, PS_ID, EA_GODINA, EA_EBROJ)
);

/*==============================================================*/
/* Table: ULOGE                                                 */
/*==============================================================*/
create table ULOGE
(
   ULO_OZNAKA           char(3) not null,
   ULO_NAZIV            varchar(120) not null,
   primary key (ULO_OZNAKA)
);

/*==============================================================*/
/* Table: UNUTRASNJA_ORGANIZACIJA                               */
/*==============================================================*/
create table UNUTRASNJA_ORGANIZACIJA
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   ORG_OJ_ID            int not null,
   SLJ_BROJ             smallint not null,
   ORG_DR_OZNAKA        char(4) not null,
   OJ_ID                int not null,
   SLJ_OD               date not null,
   SLJ_DO               date,
   primary key (DR_OZNAKA, PS_ID, ORG_OJ_ID, SLJ_BROJ)
);

/*==============================================================*/
/* Table: VERZIJA                                               */
/*==============================================================*/
create table VERZIJA
(
   SOF_DR_OZNAKA        char(4) not null,
   POS_PS_ID            int not null,
   SPR_KATBR            char(10) not null,
   SPR_TIP              char(1) not null,
   VER_OZNAKA           int not null,
   DR_OZNAKA            char(4),
   PS_ID                int,
   VER_DATFORM          date not null,
   VER_DATUK            date,
   primary key (SOF_DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA)
);

/*==============================================================*/
/* Table: VEZANE_DISCIPLINE                                     */
/*==============================================================*/
create table VEZANE_DISCIPLINE
(
   KZ_IDENT             int not null,
   POV_RBR              smallint not null,
   OBL_KZ_IDENT         int not null,
   KA_OBLAST            char(2) not null,
   primary key (KZ_IDENT, POV_RBR)
);

/*==============================================================*/
/* Table: VEZANI_ELEMENTI                                       */
/*==============================================================*/
create table VEZANI_ELEMENTI
(
   KZ_IDENT             int not null,
   POV_RBR              smallint not null,
   PSE_RBR              smallint not null,
   POE_RBR              smallint not null,
   ELE_KZ_IDENT         int not null,
   KA_OBLAST            char(2) not null,
   SO_OZNAKA            numeric(2,0) not null,
   EZ_OZNAKA            numeric(2,0) not null,
   primary key (KZ_IDENT, POV_RBR, PSE_RBR, POE_RBR)
);

/*==============================================================*/
/* Table: VEZANI_SEGMENTI                                       */
/*==============================================================*/
create table VEZANI_SEGMENTI
(
   KZ_IDENT             int not null,
   POV_RBR              smallint not null,
   PSE_RBR              smallint not null,
   SEG_KZ_IDENT         int not null,
   KA_OBLAST            char(2) not null,
   SO_OZNAKA            numeric(2,0) not null,
   primary key (KZ_IDENT, POV_RBR, PSE_RBR)
);

/*==============================================================*/
/* Table: VRSTA_ANGAZOVANJA                                     */
/*==============================================================*/
create table VRSTA_ANGAZOVANJA
(
   VA_OZNAKA            char(2) not null,
   VA_NAZIV             varchar(40) not null,
   primary key (VA_OZNAKA)
);

/*==============================================================*/
/* Table: VRSTA_PARTNERSTVA                                     */
/*==============================================================*/
create table VRSTA_PARTNERSTVA
(
   VP_ID                smallint not null,
   VP_NAZIV             varchar(40) not null,
   primary key (VP_ID)
);

/*==============================================================*/
/* Table: ZAINTERESOVANE_STRANE                                 */
/*==============================================================*/
create table ZAINTERESOVANE_STRANE
(
   DR_OZNAKA            char(4) not null,
   PS_ID                int not null,
   ZAIN_ID              int not null,
   ZAIN_TIP             char(1) not null default 'K',
   ULO_OZNAKA           char(3),
   POS_DR_OZNAKA        char(4),
   POS_PS_ID            int,
   ZAIN_PERSONALNI      varchar(40),
   primary key (DR_OZNAKA, PS_ID, ZAIN_ID, ZAIN_TIP)
);

alter table AKTIVNOSTI_U_ETAPI add constraint FK_AKTIVNOSTI_U_ETAPI foreign key (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID)
      references ETAPE_U_PROJEKTU (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID) on delete restrict on update restrict;

alter table AKTIVNOSTI_U_ETAPI add constraint FK_U_ETAPI foreign key (AKT_OZNAKA)
      references KATALOG_AKTIVNOSTI (AKT_OZNAKA) on delete restrict on update restrict;

alter table DODELJENA add constraint FK_DODELJEN foreign key (DR_OZNAKA, PS_ID, LJ_ID)
      references LJUDSKI_RESURSI (DR_OZNAKA, PS_ID, LJ_ID) on delete restrict on update restrict;

alter table DODELJENA add constraint FK_EKIPA foreign key (AKT_DR_OZNAKA, AKT_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID, AKT_OZNAKA, AKTET_RBR)
      references AKTIVNOSTI_U_ETAPI (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID, AKT_OZNAKA, AKTET_RBR) on delete restrict on update restrict;

alter table ELEMENT_ZNANJA add constraint FK_ELEMENTI_ZNANJA foreign key (KZ_IDENT, KA_OBLAST, SO_OZNAKA)
      references SEGMENT_ZNANJA (KZ_IDENT, KA_OBLAST, SO_OZNAKA) on delete restrict on update restrict;

alter table ETAPE_U_PROJEKTU add constraint FK_ETAPE_PROJEKTA foreign key (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA)
      references PROJEKAT_REALIZACIJE_SOFTVERA (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA) on delete restrict on update restrict;

alter table ISPORUCENO add constraint FK_ISPORUCENA_KONFIGURACIJA foreign key (SOF_DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA, KONF_ID)
      references KONFIGURACIJA (SOF_DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA, KONF_ID) on delete restrict on update restrict;

alter table ISPORUCENO add constraint FK_KOME_SE_ISPORUCUJE foreign key (POS_DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table ISPORUCENO add constraint FK_PREDMET_PLASMANA foreign key (DR_OZNAKA, PLA_PS_ID, PLA_GODINA, PLA_BROJ_PLASMANA)
      references PLASMAN_KONFIGURACIJE (DR_OZNAKA, PS_ID, PLA_GODINA, PLA_BROJ_PLASMANA) on delete restrict on update restrict;

alter table KOMPETENCIJE_ZA_AKTIVNOST add constraint FK_PODRAZUMEVA foreign key (AKT_OZNAKA)
      references KATALOG_AKTIVNOSTI (AKT_OZNAKA) on delete restrict on update restrict;

alter table KOMPETENCIJE_ZA_AKTIVNOST add constraint FK_POTREBNA_ZA_AKTIVNOST foreign key (KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA)
      references ELEMENT_ZNANJA (KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA) on delete restrict on update restrict;

alter table KONFIGURACIJA add constraint FK_SASTAV_VERZIJE foreign key (SOF_DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA)
      references VERZIJA (SOF_DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA) on delete restrict on update restrict;

alter table KO_SE_PITA add constraint FK_KO_JE_GDE foreign key (PRO_DR_OZNAKA, PRO_PS_ID, ZAIN_ID, ZAIN_TIP)
      references ZAINTERESOVANE_STRANE (DR_OZNAKA, PS_ID, ZAIN_ID, ZAIN_TIP) on delete restrict on update restrict;

alter table KO_SE_PITA add constraint FK_KO_SE_PITA foreign key (PRO_DR_OZNAKA, PRO_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, DZ_ID, ZAHTEV_ID, ZAHTEV_VERZIJA)
      references PROJEKTNI_ZAHTEVI (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, DZ_ID, ZAHTEV_ID, ZAHTEV_VERZIJA) on delete restrict on update restrict;

alter table KO_SE_PITA add constraint FK_ULOGA_U_ZAHTEVU foreign key (ULO_OZNAKA)
      references ULOGE (ULO_OZNAKA) on delete restrict on update restrict;

alter table LJUDSKI_RESURSI add constraint FK_EVIDENCIJA_RESURSA foreign key (DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table MAPA_KOMPETENCIJA add constraint FK_SA_KOMPETENCIJOM foreign key (KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA)
      references ELEMENT_ZNANJA (KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA) on delete restrict on update restrict;

alter table MAPA_KOMPETENCIJA add constraint FK_U_MAPI foreign key (AKT_DR_OZNAKA, AKT_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID, AKT_OZNAKA, AKTET_RBR, DOD_BROJ_DODELE)
      references DODELJENA (AKT_DR_OZNAKA, AKT_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID, AKT_OZNAKA, AKTET_RBR, DOD_BROJ_DODELE) on delete restrict on update restrict;

alter table NASELJENO_MESTO add constraint FK_PRIPADA_DRZAVI foreign key (DR_OZNAKA)
      references DRZAVA (DR_OZNAKA) on delete restrict on update restrict;

alter table OBLAST_ZNANJA add constraint FK_DOMENSKE_OBLASTI foreign key (KZ_IDENT)
      references KORPUS_ZNANJA (KZ_IDENT) on delete restrict on update restrict;

alter table ORGANIZACIONE_JEDINICE add constraint FK_DELI_SE_NA foreign key (DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table ORGANIZACIONE_JEDINICE add constraint FK_SEDISTE_JEDINICE foreign key (NAS_DR_OZNAKA, NM_ID)
      references NASELJENO_MESTO (DR_OZNAKA, NM_ID) on delete restrict on update restrict;

alter table PLASMAN_KONFIGURACIJE add constraint FK_INVESTITOR foreign key (POS_DR_OZNAKA, POS_PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table PLASMAN_KONFIGURACIJE add constraint FK_PLASIRANE_KONFIGURACIJE foreign key (DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table PODRZANE_U add constraint FK_DELATNOSTI_PO_ORGJED foreign key (ORG_DR_OZNAKA, PS_ID, OJ_ID)
      references ORGANIZACIONE_JEDINICE (DR_OZNAKA, PS_ID, OJ_ID) on delete restrict on update restrict;

alter table PODRZANE_U add constraint FK_U_ORGJED foreign key (ORG_DR_OZNAKA, PS_ID, REGD_ID, REG_DATUM_REG)
      references REGISTROVAN_ZA_DELATNOST (DR_OZNAKA, PS_ID, REGD_ID, REG_DATUM_REG) on delete restrict on update restrict;

alter table POSLOVNI_PARTNERI add constraint FK_KOMPANIJA foreign key (DR_OZNAKA, POS_PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table POSLOVNI_PARTNERI add constraint FK_PARTNER foreign key (POS_DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table POSLOVNI_PARTNERI add constraint FK_PARTNERSKI_ODNOS foreign key (VP_ID)
      references VRSTA_PARTNERSTVA (VP_ID) on delete restrict on update restrict;

alter table POSLOVNI_SUBJEKAT add constraint FK_POVEZANE_KOMPANIJE foreign key (POS_DR_OZNAKA, POS_PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table POSLOVNI_SUBJEKAT add constraint FK_REGISTROVANE_KOMPANIJE foreign key (DR_OZNAKA)
      references DRZAVA (DR_OZNAKA) on delete restrict on update restrict;

alter table POSLOVNI_SUBJEKAT add constraint FK_SEDISTE_KOMPANIJE foreign key (DR_OZNAKA, NM_ID)
      references NASELJENO_MESTO (DR_OZNAKA, NM_ID) on delete restrict on update restrict;

alter table POTREBNE_KOMPETENCIJE add constraint FK_POTREBNO foreign key (DR_OZNAKA, PS_ID, RM_ID)
      references RADNA_MESTA (DR_OZNAKA, PS_ID, RM_ID) on delete restrict on update restrict;

alter table POTREBNE_KOMPETENCIJE add constraint FK_PO_RADNIM_MESTIMA foreign key (KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA)
      references ELEMENT_ZNANJA (KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA) on delete restrict on update restrict;

alter table POVEZANI_KORPUSI_ZNANJA add constraint FK_OSNOVNI_KORPUS_ZNANJA foreign key (KZ_IDENT)
      references KORPUS_ZNANJA (KZ_IDENT) on delete restrict on update restrict;

alter table POVEZANI_KORPUSI_ZNANJA add constraint FK_POVEZANI_KORPUSI_ZNANJA foreign key (KOR_KZ_IDENT)
      references KORPUS_ZNANJA (KZ_IDENT) on delete restrict on update restrict;

alter table PROFIL_KOMPETENCIJA add constraint FK_KOMPETENCIJA foreign key (KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA)
      references ELEMENT_ZNANJA (KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA) on delete restrict on update restrict;

alter table PROFIL_KOMPETENCIJA add constraint FK_KOMPETENCIJE foreign key (DR_OZNAKA, PS_ID, LJ_ID)
      references LJUDSKI_RESURSI (DR_OZNAKA, PS_ID, LJ_ID) on delete restrict on update restrict;

alter table PROFIL_KOMPETENCIJA add constraint FK_PROCENIO foreign key (DR_OZNAKA, PS_ID, LJU_LJ_ID)
      references LJUDSKI_RESURSI (DR_OZNAKA, PS_ID, LJ_ID) on delete restrict on update restrict;

alter table PROIZVODI_U_ETAPI add constraint FK_RAZVOJ_U_ETAPI foreign key (ETA_DR_OZNAKA, ETA_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID)
      references ETAPE_U_PROJEKTU (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID) on delete restrict on update restrict;

alter table PROIZVODI_U_ETAPI add constraint FK_STA_JE_U_ETAPI foreign key (STA_SPR_KATBR, STA_SPR_TIP, ETA_DR_OZNAKA, ETA_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, STA_VER_OZNAKA)
      references STA_JE_PREDMET_PROJEKTA (SPR_KATBR, SPR_TIP, DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, VER_OZNAKA) on delete restrict on update restrict;

alter table PROJEKAT_REALIZACIJE_SOFTVERA add constraint FK_PROJEKTI foreign key (DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table PROJEKAT_REALIZACIJE_SOFTVERA add constraint FK_TEMPLEJT_PROCESA foreign key (DR_OZNAKA, PS_ID, ID_PROCESA)
      references SOFTVERSKI_PROCES (DR_OZNAKA, PS_ID, ID_PROCESA) on delete restrict on update restrict;

alter table PROJEKAT_REALIZACIJE_SOFTVERA add constraint FK_TIP_PROJ foreign key (TIPP_D)
      references TIP_PROJEKTA (TIPP_D) on delete restrict on update restrict;

alter table PROJEKTNI_ZAHTEVI add constraint FK_DOMEN foreign key (DZ_ID)
      references DOMEN_ZAHTEVA (DZ_ID) on delete restrict on update restrict;

alter table PROJEKTNI_ZAHTEVI add constraint FK_KATEGORISAN foreign key (KAT_ID)
      references KLASIFIKATOR (KAT_ID) on delete restrict on update restrict;

alter table PROJEKTNI_ZAHTEVI add constraint FK_PRIOIRITET foreign key (PRIOR_ID)
      references PRIORITET (PRIOR_ID) on delete restrict on update restrict;

alter table PROJEKTNI_ZAHTEVI add constraint FK_U_KOM_JE_STATUSU foreign key (ISTAT_ID)
      references STATUS_ZAHTEVA (ISTAT_ID) on delete restrict on update restrict;

alter table PROJEKTNI_ZAHTEVI add constraint FK_ZAHTEVI_ZA_PROJEKAT foreign key (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA)
      references PROJEKAT_REALIZACIJE_SOFTVERA (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA) on delete restrict on update restrict;

alter table RADNA_MESTA add constraint FK_ZAPOSLJAVA_NA foreign key (DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table RASPORED_PO_JEDINICAMA add constraint FK_IMA_RM foreign key (ORG_DR_OZNAKA, PS_ID, OJ_ID)
      references ORGANIZACIONE_JEDINICE (DR_OZNAKA, PS_ID, OJ_ID) on delete restrict on update restrict;

alter table RASPORED_PO_JEDINICAMA add constraint FK_RM_U_JED foreign key (ORG_DR_OZNAKA, PS_ID, RM_ID)
      references RADNA_MESTA (DR_OZNAKA, PS_ID, RM_ID) on delete restrict on update restrict;

alter table REGISTAR_DELATNOSTI add constraint FK_REGISTROVANE_DELATNOSTI foreign key (DR_OZNAKA)
      references DRZAVA (DR_OZNAKA) on delete restrict on update restrict;

alter table REGISTROVAN_ZA_DELATNOST add constraint FK_KO_JE_REGISTROVAN foreign key (DR_OZNAKA, REGD_ID)
      references REGISTAR_DELATNOSTI (DR_OZNAKA, REGD_ID) on delete restrict on update restrict;

alter table REGISTROVAN_ZA_DELATNOST add constraint FK_REGISTROVAN_ZA foreign key (DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table SASTAV add constraint FK_KOMPONENTA foreign key (VER_SOF_DR_OZNAKA, VER_POS_PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA)
      references VERZIJA (SOF_DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA) on delete restrict on update restrict;

alter table SASTAV add constraint FK_KONFIGURACIJA foreign key (SOF_DR_OZNAKA, POS_PS_ID, KON_SPR_KATBR, KON_SPR_TIP, KON_VER_OZNAKA, KONF_ID)
      references KONFIGURACIJA (SOF_DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA, KONF_ID) on delete restrict on update restrict;

alter table SASTAV__U_VERZIJI add constraint FK_AKTIVNOST_U_SASTAVU foreign key (AKT_OZNAKA)
      references KATALOG_AKTIVNOSTI (AKT_OZNAKA) on delete restrict on update restrict;

alter table SASTAV__U_VERZIJI add constraint FK_KONFIGURACIJA_AKTIVNOSTI foreign key (STR_AKT_OZNAKA, AKT_VERZIJA)
      references STRUKTURA_AKTIVNOSTI (AKT_OZNAKA, AKT_VERZIJA) on delete restrict on update restrict;

alter table SEGMENT_ZNANJA add constraint FK_STRUKTURA_OBLASTI foreign key (KZ_IDENT, KA_OBLAST)
      references OBLAST_ZNANJA (KZ_IDENT, KA_OBLAST) on delete restrict on update restrict;

alter table SOFTVERSKI_PROCES add constraint FK_MODELI_PROCESA foreign key (DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table SOFTVERSKI_PROIZVOD add constraint FK_ASORTIMAN_PROIZVODA foreign key (DR_OZNAKA, POS_PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table SOFTVERSKI_PROIZVOD add constraint FK_PROIZVODJAC foreign key (POS_DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table STA_JE_PREDMET_PROJEKTA add constraint FK_PROIZVODI foreign key (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA)
      references PROJEKAT_REALIZACIJE_SOFTVERA (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA) on delete restrict on update restrict;

alter table STA_JE_PREDMET_PROJEKTA add constraint FK_U_PROJEKTU foreign key (DR_OZNAKA, PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA)
      references VERZIJA (SOF_DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP, VER_OZNAKA) on delete restrict on update restrict;

alter table STA_SE_PREDAJE_U_AKTIVNOSTI add constraint FK_ELEMENT_PRIMOPREDAJE foreign key (AKT_DR_OZNAKA, AKT_PS_ID, AKT_TIPP_D, AKT_PROJ_ID, AKT_PROJ_REVIZIJA, AKT_ETAPA_ID2, AKT_AKT_OZNAKA, AKT_AKTET_RBR)
      references AKTIVNOSTI_U_ETAPI (DR_OZNAKA, PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID, AKT_OZNAKA, AKTET_RBR) on delete restrict on update restrict;

alter table STA_SE_PREDAJE_U_AKTIVNOSTI add constraint FK_IZ_BAZENA_ETAPE foreign key (AKT_DR_OZNAKA, AKT_PS_ID, AKT_TIPP_D, AKT_PROJ_ID, AKT_PROJ_REVIZIJA, AKT_ETAPA_ID2, PRO_STA_SPR_KATBR, PRO_STA_SPR_TIP, STA_VER_OZNAKA)
      references PROIZVODI_U_ETAPI (ETA_DR_OZNAKA, ETA_PS_ID, TIPP_D, PROJ_ID, PROJ_REVIZIJA, ETAPA_ID, STA_SPR_KATBR, STA_SPR_TIP, STA_VER_OZNAKA) on delete restrict on update restrict;

alter table STRUKTURA_AKTIVNOSTI add constraint FK_SLOZENA_AKTIVNOST foreign key (AKT_OZNAKA)
      references KATALOG_AKTIVNOSTI (AKT_OZNAKA) on delete restrict on update restrict;

alter table STRUKTURA_PROCESA add constraint FK_AKTIVNOST_U_MODELU foreign key (AKT_OZNAKA, AKT_VERZIJA)
      references STRUKTURA_AKTIVNOSTI (AKT_OZNAKA, AKT_VERZIJA) on delete restrict on update restrict;

alter table STRUKTURA_PROCESA add constraint FK_MODEL_PROCESA foreign key (DR_OZNAKA, PS_ID, ID_PROCESA)
      references SOFTVERSKI_PROCES (DR_OZNAKA, PS_ID, ID_PROCESA) on delete restrict on update restrict;

alter table UGOVORI_O_ANGAZOVANJU add constraint FK_EVIDENCIJA_ANGAZOVANJA foreign key (POS_DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table UGOVORI_O_ANGAZOVANJU add constraint FK_GDE foreign key (POS_DR_OZNAKA, PS_ID, OJ_ID)
      references ORGANIZACIONE_JEDINICE (DR_OZNAKA, PS_ID, OJ_ID) on delete restrict on update restrict;

alter table UGOVORI_O_ANGAZOVANJU add constraint FK_KAKO_JE_ANGAZOVAN foreign key (VA_OZNAKA)
      references VRSTA_ANGAZOVANJA (VA_OZNAKA) on delete restrict on update restrict;

alter table UGOVORI_O_ANGAZOVANJU add constraint FK_KO_JE_ANGAZOVAN foreign key (POS_DR_OZNAKA, PS_ID, LJ_ID)
      references LJUDSKI_RESURSI (DR_OZNAKA, PS_ID, LJ_ID) on delete restrict on update restrict;

alter table UGOVORI_O_ANGAZOVANJU add constraint FK_NA_RADNOM_MESTU foreign key (POS_DR_OZNAKA, PS_ID, RM_ID)
      references RADNA_MESTA (DR_OZNAKA, PS_ID, RM_ID) on delete restrict on update restrict;

alter table UGOVORI_O_ANGAZOVANJU add constraint FK_ODGOVORNO_LICE foreign key (POS_DR_OZNAKA, PS_ID, LJU_LJ_ID)
      references LJUDSKI_RESURSI (DR_OZNAKA, PS_ID, LJ_ID) on delete restrict on update restrict;

alter table UNUTRASNJA_ORGANIZACIJA add constraint FK_JEDINICA_U_SASTAVU foreign key (DR_OZNAKA, PS_ID, OJ_ID)
      references ORGANIZACIONE_JEDINICE (DR_OZNAKA, PS_ID, OJ_ID) on delete restrict on update restrict;

alter table UNUTRASNJA_ORGANIZACIJA add constraint FK_SLOZENA_JEDINICA foreign key (DR_OZNAKA, PS_ID, ORG_OJ_ID)
      references ORGANIZACIONE_JEDINICE (DR_OZNAKA, PS_ID, OJ_ID) on delete restrict on update restrict;

alter table VERZIJA add constraint FK_VERZIJE foreign key (SOF_DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP)
      references SOFTVERSKI_PROIZVOD (DR_OZNAKA, POS_PS_ID, SPR_KATBR, SPR_TIP) on delete restrict on update restrict;

alter table VERZIJA add constraint FK_VERZIONIRAO foreign key (DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table VEZANE_DISCIPLINE add constraint FK_POVEZANA_OBLAST foreign key (OBL_KZ_IDENT, KA_OBLAST)
      references OBLAST_ZNANJA (KZ_IDENT, KA_OBLAST) on delete restrict on update restrict;

alter table VEZANE_DISCIPLINE add constraint FK_POVEZANE_OBLASTI foreign key (KZ_IDENT)
      references KORPUS_ZNANJA (KZ_IDENT) on delete restrict on update restrict;

alter table VEZANI_ELEMENTI add constraint FK_POVEZANI_ELEMENT foreign key (ELE_KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA)
      references ELEMENT_ZNANJA (KZ_IDENT, KA_OBLAST, SO_OZNAKA, EZ_OZNAKA) on delete restrict on update restrict;

alter table VEZANI_ELEMENTI add constraint FK_POVEZANI_ELEMENTI foreign key (KZ_IDENT, POV_RBR, PSE_RBR)
      references VEZANI_SEGMENTI (KZ_IDENT, POV_RBR, PSE_RBR) on delete restrict on update restrict;

alter table VEZANI_SEGMENTI add constraint FK_POVEZANI_SEGMENT foreign key (SEG_KZ_IDENT, KA_OBLAST, SO_OZNAKA)
      references SEGMENT_ZNANJA (KZ_IDENT, KA_OBLAST, SO_OZNAKA) on delete restrict on update restrict;

alter table VEZANI_SEGMENTI add constraint FK_POVEZANI_SEGMENTI foreign key (KZ_IDENT, POV_RBR)
      references VEZANE_DISCIPLINE (KZ_IDENT, POV_RBR) on delete restrict on update restrict;

alter table ZAINTERESOVANE_STRANE add constraint FK_EVIDENCIJA_ZAINTERESOVANIH_STRANA foreign key (DR_OZNAKA, PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

alter table ZAINTERESOVANE_STRANE add constraint FK_U_ULOZI foreign key (ULO_OZNAKA)
      references ULOGE (ULO_OZNAKA) on delete restrict on update restrict;

alter table ZAINTERESOVANE_STRANE add constraint FK_ZAINTERESOANA_KOMPANIJA foreign key (POS_DR_OZNAKA, POS_PS_ID)
      references POSLOVNI_SUBJEKAT (DR_OZNAKA, PS_ID) on delete restrict on update restrict;

