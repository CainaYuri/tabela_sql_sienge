USE [DW_SIENGE_BI]
GO
****** Object:  Table [dbo].[BD_BANKMOVEMENTS_ONLYDETACHEDMOVEMENT]   
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BD_BANKMOVEMENTS_ONLYDETACHEDMOVEMENT](
	[bankMovementId] [int] NULL,
	[billId] [int] NULL,
	[installmentId] [int] NULL,
	[bankMovementAmount] [decimal](18, 10) NULL,
	[documentIdentificationId] [varchar](1000) NULL,
	[documentIdentificationName] [varchar](1000) NULL,
	[bankMovementOriginId] [varchar](1000) NULL,
	[bankMovementHistoricId] [varchar](1000) NULL,
	[bankMovementHistoricName] [varchar](1000) NULL,
	[bankMovementOperationId] [int] NULL,
	[bankMovementOperationName] [varchar](1000) NULL,
	[bankMovementOperationType] [varchar](1000) NULL,
	[bankMovementReconcile] [varchar](1000) NULL,
	[bankMovementDate] [varchar](1000) NULL,
	[billDate] [varchar](1000) NULL,
	[accountNumber] [varchar](1000) NULL,
	[companyId] [int] NULL,
	[companyName] [varchar](1000) NULL,
	[groupCompanyId] [int] NULL,
	[groupCompanyName] [varchar](1000) NULL,
	[holdingId] [int] NULL,
	[holdingName] [varchar](1000) NULL,
	[subsidiaryId] [int] NULL,
	[subsidiaryName] [varchar](1000) NULL,
	[creditorId] [int] NULL,
	[creditorName] [varchar](1000) NULL,
	[clientId] [int] NULL,
	[clientName] [varchar](1000) NULL,
	[log_data_inclusao] [datetime] NULL,
	[controle_execucao] [int] NULL
) ON [PRIMARY]
