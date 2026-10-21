# Operación Granada — auditoría del repositorio de distribución

**Corte:** 2026-10-21 UTC. **Tipo de repositorio:** público de binarios/manifiestos, **NO fuente** de Michel's Life. [Auditoría de app, plugins y CI en repo fuente](https://github.com/michels-lab/michel-s-life/blob/main/docs/GRANADA_APP_PLUGIN_AUDIT_2026-10-21.md) · [Política central sin suscripciones extra](https://github.com/michels-lab/Michel-Software-Standards/blob/main/docs/CHATGPT_PLUGIN_LEDGER.md).

## Verificación directa
- [GitHub releases/latest](https://github.com/michels-lab/michel-s-life-releases/releases/latest) devolvió `v3.0.221`, publicada el 2026-10-19: Windows v3.0.221 y Android Direct v0.2.9; **13 activos**: Setup, Portable, alias, APK, checksums, manifiesto, certificado público, AppBundle, icono y provenance.
- El README de este repo todavía nombraba **v3.0.217/Android v0.2.5** en el corte: hallazgo de documentación desactualizada, no indicio por sí mismo de un binario alterado.
- No se descargaron ni ejecutaron instaladores; la lista de activos publicada no prueba dispositivo físico, persistencia, sincronización en vivo ni origen de firma por medición local.

## Herramientas y fronteras
- **GitHub ChatGPT** está instalado y se utilizó para inspección, documentación y mantenimiento de repos.
- **Supabase ChatGPT** puede ayudar en el repo fuente bajo permiso; **no** es requisito ni herramienta de publicación de binarios aquí.
- Google/Docs/Spreadsheets instalados en ChatGPT son auxiliares externos, NO partes del instalador; no sumar SaaS/hosting/suscripciones ni incluir datos privados.
- Mantener feeds/aliases de compatibilidad existentes. No publicar LouderMe aquí; enlaces heredados de clientes antiguos deben conservarse según el propio README.
- Firmas, checksums, procedencia y aprobación del release son responsabilidad del pipeline de la app; una actualización de esta bitácora NO puede autorizar un release.

**Estado:** INVENTARIO REMOTO DOCUMENTADO / README CORREGIBLE / SIN NUEVO RELEASE / SIN PRUEBA FÍSICA. Auditar estado y hashes reales antes de cualquier publicación.
