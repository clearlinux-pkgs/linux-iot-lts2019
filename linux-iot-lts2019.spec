# This is a linux kernel with the preempt_rt patch set plus PK patches

Name:           linux-iot-lts2019
Version:        5.1.0
Release:        4
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://git.kernel.org/torvalds/t/linux-5.1.tar.gz
Source1:        config
Source2:        cmdline-iot-lts2019
Source3:        fragment-sos

%define ktarget0 iot-lts2019
%define kversion0 %{version}-%{release}.%{ktarget0}

BuildRequires:  buildreq-kernel

Requires: systemd-bin

# don't strip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

# quilt.url: https://github.com/intel/linux-intel-quilt
# quilt.branch: mainline-tracking
# quilt.tag:  mainline-tracking-v5.1-rc4-190411T171208Z

# PK XXXX: Series
Patch0001: 0001-ASoC-Intel-Skylake-Interface-change-between-firmware.patch
Patch0002: 0002-Integration-of-CBC-line-discipline-kernel-module.patch
Patch0003: 0003-mm-export-some-vm_area-APIs.patch
Patch0004: 0004-TEE-OPTEE-Adds-a-kernel-internal-TEE-client-interfac.patch
Patch0005: 0005-test-configs-use-for-clean-and-android-bare-metal-BA.patch
Patch0006: 0006-trusty-Add-trusty-driver.patch
Patch0007: 0007-usb-gadget-f_fs-don-t-free-buffer-prematurely.patch
Patch0008: 0008-ASoC-utils-add-inputs-and-outputs-to-dummy-codec.patch
Patch0009: 0009-cbc-Avoid-rx-sequence-counter-mismatch-warnings.patch
Patch0010: 0010-fTPM-add-OPTEE-fTPM-driver.patch
Patch0011: 0011-trusty-Add-notifier-before-and-after-every-smc-call.patch
Patch0012: 0012-v4l-subdev-Add-support-for-sub-streams.patch
Patch0013: 0013-ASoC-SKL-Fix-ch_cfg-when-fixup-is-applied.patch
Patch0014: 0014-Fix-for-cbc-kernel-driver-crash-during-warm-reboot.patch
Patch0015: 0015-keystore-add-keystore-driver-support.patch
Patch0016: 0016-trusty-Get-version-string-from-trusty.patch
Patch0017: 0017-v4l-subdev-Add-GS-_ROUTING-subdev-ioctls-and-operati.patch
Patch0018: 0018-ASoC-Intel-Skylake-Add-NHLT-override-control.patch
Patch0019: 0019-Fix-the-race-in-cbc-buffer-queue.patch
Patch0020: 0020-keystore-remove-type-argument-of-access_ok.patch
Patch0021: 0021-media-Use-routing-info-during-graph-traversal.patch
Patch0022: 0022-trusty-Add-interrupt-support.patch
Patch0023: 0023-ASoC-Intel-Skylake-Add-debugfs-NHLT-ssp-override.patch
Patch0024: 0024-keystore-fix-memory-leaks.patch
Patch0025: 0025-trusty-Add-fiq-support.patch
Patch0026: 0026-v4l-for-multiplex-pad-add-routing-informaion-in-link.patch
Patch0027: 0027-ASoC-Intel-Skylake-Add-debugfs-NHLT-dmic-override.patch
Patch0028: 0028-keystore-fix-missing-break.patch
Patch0029: 0029-media-entity-graph-walk-starting-from-pad.patch
Patch0030: 0030-trusty-arm64-fiq-support.patch
Patch0031: 0031-ASoC-Intel-Skylake-Read-blobs-from-debugfs-on-overri.patch
Patch0032: 0032-keystore-add-application-authentication-feature.patch
Patch0033: 0033-media-v4l-Add-new-vectorised-pixel-formats.patch
Patch0034: 0034-trusty-fiq-arm64-Allow-multiple-fiq-handlers.patch
Patch0035: 0035-ASoC-Intel-Skylake-NHLT-override-check-cfg-size-in-d.patch
Patch0036: 0036-keystore-improvement-for-depressing-compile-warning.patch
Patch0037: 0037-trusty-Add-trusty-logging-driver.patch
Patch0038: 0038-v4l2-ctrl-Add-platform-specific-v4l2-control.patch
Patch0039: 0039-ASoC-Intel-Skylake-add-ssp-blob-override-support-for.patch
Patch0040: 0040-keystore-Fix-copy-wrong-size-of-keystore-client-id.patch
Patch0041: 0041-trusty-add-couple-non-secure-memory-related-helper-r.patch
Patch0042: 0042-v4l-Extend-struct-v4l2_mbus_frame_desc_entry.patch
Patch0043: 0043-crlmodule-common-register-list-based-sensor-driver.patch
Patch0044: 0044-keystore-fix-obsoleted-timer-api-getnstimeofday64.patch
Patch0045: 0045-trusty-add-trusty-virtio-driver.patch
Patch0046: 0046-WORKAROUND-Remove-size-check-for-DMIC-blob.patch
Patch0047: 0047-ASoC-Fix-TLV-control-size-in-TLV-handler.patch
Patch0048: 0048-keystore-Fix-ISO-C90-forbidden-variable-length-array.patch
Patch0049: 0049-trusty-add-trusty-ipc-driver.patch
Patch0050: 0050-v4l-add-TI964-913-SER-DES-driver.patch
Patch0051: 0051-ALSA-core-let-low-level-driver-or-userspace-disable-.patch
Patch0052: 0052-keystore-Fix-in-compatible-size_t-print-format-for-i.patch
Patch0053: 0053-trusty-Select-api-version.patch
Patch0054: 0054-v4l-add-MAX9286-96705-SER-DES-driver.patch
Patch0055: 0055-ALSA-pcm-conditionally-avoid-mmap-of-control-data.patch
Patch0056: 0056-trusty-Handle-fiqs-without-calling-notifier-and-enab.patch
Patch0057: 0057-v4l-add-TI960-953-SER-DES-driver.patch
Patch0058: 0058-ALSA-hda-ext-add-spib-to-stream-context.patch
Patch0059: 0059-trusty-Add-smp-support.patch
Patch0060: 0060-v4l-add-IPU-driver-for-BXT-platform.patch
Patch0061: 0061-ASoC-Intel-Skylake-add-support-for-spib-mode.patch
Patch0062: 0062-trusty-irq-Add-support-for-secure-interrupt-mapping.patch
Patch0063: 0063-v4l-add-IPU-platform-configuration-data.patch
Patch0064: 0064-ASoC-Intel-Skylake-Support-for-24KHz-SoC-DMIC-captur.patch
Patch0065: 0065-media-add-member-for-trace-of-dual-multi-camera-for-.patch
Patch0066: 0066-Modify-the-static-analysis-errors-for-google-s-trust.patch
Patch0067: 0067-ASoC-Intel-Skylake-fix-for-large-get-config-api.patch
Patch0068: 0068-media-videobuf2-transfer-sub-streams-id.patch
Patch0069: 0069-Modify-Google-s-trusty-drivers-so-as-to-support-Inte.patch
Patch0070: 0070-ASoC-Intel-Skylake-generic-IPC-message-support.patch
Patch0071: 0071-Fix-the-issue-for-tipc-test-case-closer1.patch
Patch0072: 0072-media-temporarily-disable-media-request-interface.patch
Patch0073: 0073-ASoC-Intel-Skylake-Add-support-to-get-fw-configurati.patch
Patch0074: 0074-media-intel-ipu4-add-timestamp-info-in-driver.patch
Patch0075: 0075-trusty-implement-trusty-OS-timer-proxy-for-performan.patch
Patch0076: 0076-ASoC-Intel-CNL-Update-dsp-ops-API-to-take-direction-.patch
Patch0077: 0077-media-ov2775-Update-v4l2-ctrl-setting.patch
Patch0078: 0078-Replace-CPU_STARTING-CPU_DYING-with-CPU_UP_PREPARE-C.patch
Patch0079: 0079-ASoC-Intel-Add-support-for-Icelake-IDs.patch
Patch0080: 0080-media-Buttress-base-addr-interface.patch
Patch0081: 0081-trusty-fix-incompatible-pointer-types.patch
Patch0082: 0082-ASoC-Intel-Boards-Add-CNL-RT274-I2S-machine-driver.patch
Patch0083: 0083-media-intel-ipu4-ox03a10-set-hflip-default.patch
Patch0084: 0084-trusty-move-async-works-off-system-workqueue.patch
Patch0085: 0085-ASoC-Intel-Skylake-Support-for-all-rates-from-8K-to-.patch
Patch0086: 0086-media-intel-ipu4-magna-Modify-for-dual-magna.patch
Patch0087: 0087-trusty-print-out-Built-in-kernel-directly.patch
Patch0088: 0088-ASoC-Intel-Skylake-Avoid-resume-capablity-for-captur.patch
Patch0089: 0089-media-ov2775-update-register-setting.patch
Patch0090: 0090-trusty-Popup-warning-when-LK-timer-interrupt-is-not-.patch
Patch0091: 0091-ASoC-Intel-Skylake-Support-all-I2S-ports-with-all-po.patch
Patch0092: 0092-media-intel-ipu4-be-soc-Set-NV16-input-format.patch
Patch0093: 0093-trusty-log-Add-vmm-panic-notifier-for-vmm-deadloop-d.patch
Patch0094: 0094-ASoC-Intel-Skylake-Add-platform-DAI-for-deepbuffer-c.patch
Patch0095: 0095-media-ti964-pdata-for-AS_1140.patch
Patch0096: 0096-trusty-fix-rcu_preempt-soft-lockup-crash-issue.patch
Patch0097: 0097-ASoC-Intel-Change-sst_ipc_tx_message_wait-api-to-ret.patch
Patch0098: 0098-media-ti964-add-magna-subdev-for-2nd-ti964.patch
Patch0099: 0099-trusty-Add-VMM-PANIC-dump-data.patch
Patch0100: 0100-ASoC-Intel-Skylake-Extract-the-receive-response-size.patch
Patch0101: 0101-media-intel-ipu4-css-scci_IPU4_master_20181029_0542-.patch
Patch0102: 0102-Modify-Trusty-drivers-so-as-to-compatible-with-Kerne.patch
Patch0103: 0103-ASoC-Intel-Skylake-Better-handling-of-stream-interru.patch
Patch0104: 0104-Limit-to-output-trusty-lk-log-on-debug-version.patch
Patch0105: 0105-media-intel-ipu4-css-scci_IPU4_master_20181030_0713-.patch
Patch0106: 0106-media-intel-ipu4-fix-build-warning.patch
Patch0107: 0107-ASoC-Intel-Skylake-Set-DUM-bit-in-EM2-register.patch
Patch0108: 0108-trusty-ipc-tipc_msg_hdr-structure-support-large-mess.patch
Patch0109: 0109-ASoC-Intel-Skylake-Add-D0i3-support-for-Icelake-plat.patch
Patch0110: 0110-media-intel-ipu4-fix-v4l2_g_ext_ctrls-params-for-ker.patch
Patch0111: 0111-trusty-ipc-change-DEFAULT_MSG_BUF_SIZE-to-68K.patch
Patch0112: 0112-ASoC-Intel-Skylake-Audio-format-mismatch-detection.patch
Patch0113: 0113-check-CPUID-while-probe-trusty-drivers.patch
Patch0114: 0114-media-intel-ipu4p-css-scci_IPU4_master_20181029_0542.patch
Patch0115: 0115-ASoC-Intel-Skylake-add-sysfs-files-for-firmware-modu.patch
Patch0116: 0116-Fix-the-compile-error-when-update-4.12.patch
Patch0117: 0117-media-intel-ipu4p-css-scci_IPU4_master_20181030_0713.patch
Patch0118: 0118-ASoC-Intel-Skylake-Debugfs-for-core-power-handling.patch
Patch0119: 0119-media-psys-Enable-new-FW-API-for-IPU-performance.patch
Patch0120: 0120-trusty-Fix-the-warnings-for-eywa-building.patch
Patch0121: 0121-ASoC-Intel-Skylake-DebugFs-changes-to-suit-FDK.patch
Patch0122: 0122-media-intel-ipu4p-css-scci_IPU4_master_20181105_1124.patch
Patch0123: 0123-trusty-Enable-dynamic-timer.patch
Patch0124: 0124-ASoC-Intel-Skylake-Support-Pipeline-Properties-IPC.patch
Patch0125: 0125-check-vmm-signature-for-vmm-dump.patch
Patch0126: 0126-media-intel-ipu4-css-scci_IPU4_master_20181108_1902-.patch
Patch0127: 0127-ASoC-Intel-board-Move-cnl_rt274-clock-setting-to-sup.patch
Patch0128: 0128-media-intel-ipu4p-css-scci_IPU4_master_20181108_1902.patch
Patch0129: 0129-Revert-BXT-DYNAMIC-TIMER-Enable-dynamic-timer.patch
Patch0130: 0130-ASoC-Intel-Skylake-Add-user-notification-event-for-p.patch
Patch0131: 0131-media-css-scci_master_20181105_2026-FwRelease.patch
Patch0132: 0132-Revert-trusty-implement-trusty-OS-timer-proxy-for-pe.patch
Patch0133: 0133-ASoC-Intel-Extract-the-nhlt-version-from-DSDT-table.patch
Patch0134: 0134-media-buttress-Use-ISR_STATUS-in-buttress-ISR.patch
Patch0135: 0135-trusty-add-support-for-parameterized-NOP-ops.patch
Patch0136: 0136-ASoC-Intel-Skylake-Increase-the-max-number-of-entrie.patch
Patch0137: 0137-media-intel-ipu4-fix-2-kernel-panic-in-ipu-driver.patch
Patch0138: 0138-trusty-switch-to-use-version-3-of-TRUSTY_API.patch
Patch0139: 0139-ASoC-Intel-Skylake-Add-single-module-support-in-a-gi.patch
Patch0140: 0140-media-intel-ipu4p-css-scci_IPU4_master_20181119_0558.patch
Patch0141: 0141-trusty-add-support-for-SM-Wall-object.patch
Patch0142: 0142-ASoC-Intel-Skylake-Fix-incorrect-parsing-of-pipe-tok.patch
Patch0143: 0143-media-Enable-streamID-switching-for-ISYS-IOMMU.patch
Patch0144: 0144-trusty-add-support-for-trusty-backup-timer.patch
Patch0145: 0145-ASoC-Intel-Skylake-Create-SSP-BE-dais-dynamically.patch
Patch0146: 0146-media-Set-IPU-device-name.patch
Patch0147: 0147-trusty-kernel-driver-code-refine.patch
Patch0148: 0148-ASoC-Intel-Board-Add-BXTP-MRB-machine-driver-for-NXP.patch
Patch0149: 0149-Change-Trusty-Kconfig-to-build-for-X86-Arch-only.patch
Patch0150: 0150-media-intel-ipu4-VIRT-Support-for-IPU-ACRN-virtualiz.patch
Patch0151: 0151-ASoC-tdf8532-NXP-TDF8532-audio-class-D-amplifier-dri.patch
Patch0152: 0152-media-intel-ipu4-refine-ipu_fw_isys_close-mutex-usag.patch
Patch0153: 0153-trusty-Add-null-check-pointer-before-deference.patch
Patch0154: 0154-ASoC-Intel-Multiple-I-O-PCM-format-support-for-pipe.patch
Patch0155: 0155-media-intel-ipu4-use-softlink-instead-of-shell-copy.patch
Patch0156: 0156-trusty-Check-if-eVmm-is-available-before-init-driver.patch
Patch0157: 0157-ASoC-Intel-Skylake-Parse-manifest-data-to-fill-DMA-c.patch
Patch0158: 0158-media-i2c-add-required-kconf-dependency.patch
Patch0159: 0159-trusty-Update-Trusty-timer-solution.patch
Patch0160: 0160-ASoC-Intel-Skylake-Add-support-for-always-on-CLK-con.patch
Patch0161: 0161-media-Disable-CSI-EOF-IRQ.patch
Patch0162: 0162-trusty-detect-vmm-when-load-trusty-driver.patch
Patch0163: 0163-ASoC-Intel-Skylake-Send-correct-size-in-ipc-header-f.patch
Patch0164: 0164-media-Disable-FW-IRQ-and-response-of-EOF.patch
Patch0165: 0165-Remove-unused-label-to-depress-compile-warning.patch
Patch0166: 0166-ASoC-Intel-board-Add-support-for-HDMI-in-cnl_rt274.patch
Patch0167: 0167-media-intel-ipu4-adv7481_hdmi-Fix-S3-resume.patch
Patch0168: 0168-trusty-Update-dependency-of-trusty-module.patch
Patch0169: 0169-ASoC-Intel-Boards-Add-ICL-RT274-I2S-machine-driver.patch
Patch0170: 0170-media-intel-ipu4-remove-redundant-assignment-in-csi-.patch
Patch0171: 0171-trusty-Rename-CWP-with-ACRN.patch
Patch0172: 0172-ASoC-Intel-Skylake-Notify-topology-changes.patch
Patch0173: 0173-media-intel-ipu4-ov495-OV2775-OV495-enablement.patch
Patch0174: 0174-trusty-add-RAX-into-clobber-list-of-inline-asm-for-A.patch
Patch0175: 0175-ASoC-Intel-Skylake-Add-support-for-module-notificati.patch
Patch0176: 0176-media-intel-ipu4-css-scci_IPU4_master_20181217_1904-.patch
Patch0177: 0177-trusty-Update-macro-SMC_FC_GET_WALL_SIZE-from-12-to-.patch
Patch0178: 0178-ASoC-Intel-Skylake-Add-a-separate-module-type-for-AS.patch
Patch0179: 0179-media-intel-ipu4p-css-scci_IPU4_master_20181217_1904.patch
Patch0180: 0180-unify-trusty-driver.patch
Patch0181: 0181-ASoC-Intel-Skylake-Add-support-for-DMA-Buffer-config.patch
Patch0182: 0182-media-intel-ipu4-css-scci_IPU4_master_20181222_1218-.patch
Patch0183: 0183-Revert-trusty-ipc-change-DEFAULT_MSG_BUF_SIZE-to-68K.patch
Patch0184: 0184-ASoC-Intel-Set-all-I2S-ports-to-slave-mode-after-DSP.patch
Patch0185: 0185-media-intel-ipu4p-css-scci_IPU4_master_20181222_1218.patch
Patch0186: 0186-refine-work-queue-in-trusty-driver.patch
Patch0187: 0187-ASoC-Intel-Skylake-Add-support-for-GAIN-module.patch
Patch0188: 0188-media-intel-ipu4-ti960-fix-map-conflict.patch
Patch0189: 0189-register-suspend-callback.patch
Patch0190: 0190-ASoC-Intel-Skylake-Fix-Max-DSP-MCPS-value.patch
Patch0191: 0191-Fix-compile-warning-from-ISO90-and-output-format.patch
Patch0192: 0192-media-v4l2-core-Fix-compile-errors.patch
Patch0193: 0193-ASoC-Intel-Skylake-Avoid-global-kcontrol-pointer-for.patch
Patch0194: 0194-check-return-value-of-hypercall.patch
Patch0195: 0195-media-intel-ipu4-VIRT-Close-dmabuf-fd-when-dmabuf-re.patch
Patch0196: 0196-ASoC-Intel-Board-Add-BXTP-MRB-ULL-machine-driver.patch
Patch0197: 0197-Fix-compilation-errors-when-rebase-to-v4.19-rc1.patch
Patch0198: 0198-media-intel-ipu4-VIRT-Avoid-double-close-of-dmabuf-F.patch
Patch0199: 0199-ASoC-Intel-Skylake-Add-support-to-configure-ADSP-Sch.patch
Patch0200: 0200-media-intel-ipu4-pdata-for-OV495-multiport.patch
Patch0201: 0201-ASoC-Intel-Skylake-Poll-on-ADSPCS.CSTALL-bit-to-conf.patch
Patch0202: 0202-media-intel-ipu4-fix-TI960-i2c-adapter.patch
Patch0203: 0203-ASoC-Intel-Skylake-Add-delay-during-DSP-core-start.patch
Patch0204: 0204-media-intel-ipu4-enable-OV495-multiport.patch
Patch0205: 0205-ALSA-hda-Make-sure-DMA-is-stopped-by-reading-back-th.patch
Patch0206: 0206-media-intel-ipu4-Fix-compile-errors.patch
Patch0207: 0207-ALSA-hda-Make-sure-DMA-is-started-by-reading-back-th.patch
Patch0208: 0208-media-intel-ipu4-restore-back-ox03a-init-sequence.patch
Patch0209: 0209-ALSA-hda-Log-HDA-Hardware-related-errors.patch
Patch0210: 0210-media-intel-ipu4-separated-init-seq-for-ox03a10-and-.patch
Patch0211: 0211-ALSA-hda-check-if-stream-is-stopped-in-snd_hdac_stre.patch
Patch0212: 0212-media-intel-ipu4-Fix-IPC-timeout-in-ipu-buttress-aut.patch
Patch0213: 0213-ASoC-Intel-Skylake-Support-multiple-format-configs.patch
Patch0214: 0214-media-intel-ipu4-ti960-ov495-frame-sync-setting.patch
Patch0215: 0215-ASoC-Intel-Skylake-Add-API-to-reset-private-instance.patch
Patch0216: 0216-media-intel-ipu4-Fixing-common-code-for-KW-scan.patch
Patch0217: 0217-ASoC-Intel-Skylake-Add-an-API-to-reset-the-usage-cou.patch
Patch0218: 0218-ASoC-Intel-Skylake-Fix-the-is_dsp_running-to-return-.patch
Patch0219: 0219-ASoC-Intel-CNL-Fix-for-the-firmware-redownload-failu.patch
Patch0220: 0220-ASoC-Intel-Skylake-Update-gain-interface-structure.patch
Patch0221: 0221-ASoC-Intel-kconfig-Make-drivers-build-on-x86-only.patch
Patch0222: 0222-ASoC-Intel-Skylake-Add-support-to-notify-resource-ev.patch
Patch0223: 0223-ASoC-Intel-BXT-Retry-FW-download-sequence.patch
Patch0224: 0224-ASoC-Intel-Skylake-Set-dsp-cores-off-during-shutdown.patch
Patch0225: 0225-ASoC-Intel-Disable-dsp-core-in-skl_shutdown.patch
Patch0226: 0226-ASoC-soc-pcm-Fix-FE-and-BE-race-when-accessing-subst.patch
Patch0227: 0227-ASoC-Intel-Boards-Add-machine-driver-for-Kabylake-R.patch
Patch0228: 0228-ASoC-rt298-Set-jack-combo-for-kabylake-R.patch
Patch0229: 0229-ASoC-Intel-Boards-Add-machine-driver-for-RSE-topolog.patch
Patch0230: 0230-ASoC-Intel-Boards-Add-machine-driver-for-HU-topology.patch
Patch0231: 0231-ASoC-Intel-Boards-Add-a-machine-driver-for-BXT-P-IVI.patch
Patch0232: 0232-ASoC-Intel-Boards-Add-machine-driver-for-generic-top.patch
Patch0233: 0233-ASoC-Intel-Skylake-Resolve-load-DMA-control-config-i.patch
Patch0234: 0234-ASoC-Intel-common-Provide-an-interface-to-send-IPCs-.patch
Patch0235: 0235-ASoC-Intel-Fix-race-condition-in-IPC-rx-list.patch
Patch0236: 0236-ASoC-Intel-Skylake-pipeline-needs-to-be-reset-before.patch
Patch0237: 0237-ASoC-Intel-Allow-for-firmware-load-retry.patch
Patch0238: 0238-ASoC-Intel-Add-ICL-machine-drivers-table.patch
Patch0239: 0239-ASoC-Intel-4.19-rc1-and-4.20-rc1-rebase-fixups.patch
Patch0240: 0240-REVERTME-Fix-no-audio-output-after-resume-from-S3.patch
Patch0241: 0241-ASoC-Intel-Skylake-Restore-static-SSP5-BE-declaratio.patch
Patch0242: 0242-ASoC-Intel-Add-support-for-imr_alloc-flag.patch
Patch0243: 0243-ASoC-Intel-Restore-static-FE-declaration-for-bxt_tdf.patch
Patch0244: 0244-ASoC-Intel-Skylake-refactor-memory-management-in-skl.patch
Patch0245: 0245-ASoC-Intel-Skylake-Export-skylake-functions-for-virt.patch
Patch0246: 0246-ASoC-Intel-Skylake-Modify-skl_platform_register.patch
Patch0247: 0247-ASoC-Intel-Skylake-Add-Kconfig-options-for-virtualiz.patch
Patch0248: 0248-ASoC-Intel-Skylake-Add-support-for-Virtio-SST.patch
Patch0249: 0249-ASoC-Intel-Skylake-Register-virtualization-BE-servic.patch
Patch0250: 0250-ASoC-Intel-Skylake-Workarounds-for-virtualization.patch
Patch0251: 0251-ASoC-Intel-Skylake-Virt-Add-virtualization-layer-to-.patch
Patch0252: 0252-ASoC-Intel-Skylake-Acquire-irq-after-RIRB-allocation.patch
Patch0253: 0253-ASoC-Add-error-handling-for-stream-events-in-soc_pcm.patch
Patch0254: 0254-ASoC-tdf8532-Account-for-critical-sections.patch
Patch0255: 0255-ASoC-Intel-Skylake-Add-dummy_dais-to-skl_machine_pda.patch
Patch0256: 0256-Asoc-Intel-Skylake-display-firmware-name-and-version.patch
Patch0257: 0257-ASoC-Intel-Skylake-Add-FE-and-BE-DAIs-for-ULL-Ultra-.patch
Patch0258: 0258-ASoC-Intel-board-Update-BXT-P-ULL-machine-driver-to-.patch
Patch0259: 0259-ASoC-Skl-Virt-Fix-incorrect-virt-msg-response-handli.patch
Patch0260: 0260-ASoC-Skl-Virt-Add-locks-to-virtqueue-related-operati.patch
Patch0261: 0261-ASoC-Skl-Virt-Add-locks-to-substreams-list.patch
Patch0262: 0262-ASoC-Skl-Virt-Handle-timed-out-message-replies.patch
Patch0263: 0263-ASoC-Intel-Skylake-Add-CNL-load-library-support.patch
Patch0264: 0264-ASoC-Intel-Skylake-Unify-fw-initialization-process.patch
Patch0265: 0265-ASoC-Intel-Skylake-Do-not-use-fw_ops-handlers-explic.patch
Patch0266: 0266-ASoC-Intel-Skl-Virt-Fix-PCI-dev-initialization.patch
Patch0267: 0267-ASoC-Intel-Skylake-Virt-Support-for-entering-exiting.patch
Patch0268: 0268-ASoC-Skl-Virt-Handle-expired-messages-in-worker-thre.patch
Patch0269: 0269-ASoC-Intel-Skylake-Add-dummy_codec-to-skl_machine_pd.patch
Patch0270: 0270-ASoC-Intel-Correct-TLV-parsing-for-non-vendor-module.patch
Patch0271: 0271-ASoC-Intel-Increase-IPC-Timeout.patch
Patch0272: 0272-ASoC-Intel-Skylake-Provide-tplg_name-module-param.patch
Patch0273: 0273-ASoC-Intel-Skylake-fix-for-BXT-HW-data-loss-in-16-16.patch
Patch0274: 0274-ASoC-Intel-Skylake-Virt-Support-for-GOS-access-right.patch
Patch0275: 0275-ASoC-Intel-Skylake-Virt-Synchronistation-of-ALSA-con.patch
Patch0276: 0276-ASoC-Intel-Skylake-Virt-Virtualization-BE-as-module.patch
Patch0277: 0277-ASoC-Intel-Skylake-Virt-Check-domain_id-during-sync-.patch
Patch0278: 0278-ASoC-Intel-Skl-Virt-Choose-topology-based-on-GOS-dom.patch
Patch0279: 0279-vhm-fix-audio-backend-module-handle-ioreq-incorrectl.patch
Patch0280: 0280-ASoC-Intel-Skl-Virt-Release-resources-is-Service-OS.patch
Patch0281: 0281-ASoC-Intel-Skl-Virt-Latency-improvement.patch
Patch0282: 0282-ASoC-Intel-Skl-Virt-Add-static-map-of-domain_ids.patch
Patch0283: 0283-ASoC-Intel-Skylake-Generic-firmware-recovery-on-IPC-.patch
Patch0284: 0284-ASoC-Intel-Skylake-print-module-type-instead-of-id.patch
Patch0285: 0285-ASoC-Intel-Skylake-Remove-MCPS-available-check.patch
Patch0286: 0286-ASoC-Intel-Skylake-Remove-memory-available-check.patch
Patch0287: 0287-ASoC-Intel-Skylake-Correct-skl_base_cfg-declaration.patch
Patch0288: 0288-ASoC-Intel-Skl-Virt-Fix-compilation-BE-and-FE-at-onc.patch
Patch0289: 0289-ASoC-Intel-Skl-Virt-Fix-warnings.patch
Patch0290: 0290-ASoC-Intel-Skylake-Increase-ROM_INIT_TIMEOUT-to-100m.patch
Patch0291: 0291-ASoC-Intel-Skylake-Fix-FW-Notification-Data-format.patch
Patch0292: 0292-ASoC-Intel-Skylake-Remove-code-disabling-FW-notifica.patch
Patch0293: 0293-ASoC-Intel-Common-Fix-NULL-dereference-for-tx_wait_d.patch
Patch0294: 0294-ASoC-Intel-Skylake-Fix-IPC-error-code-definitions.patch
Patch0295: 0295-ASoC-Intel-Skylake-Raise-log-level-for-FW-notificati.patch
Patch0296: 0296-ASoC-Intel-Skl-Virt-Fix-panic-issue-on-HW-pos-update.patch
Patch0297: 0297-ASoC-Intel-Skl-Virt-Remove-support-for-DSP-IPC-on-FE.patch
Patch0298: 0298-ASoC-Intel-Skl-Virt-Fix-panic-during-tplg-initializa.patch
Patch0299: 0299-ASoC-Intel-Skylake-Virt-Change-SCHED-policy-to-FIFO.patch
Patch0300: 0300-ASoC-Intel-Skl-Virt-Don-t-duplicate-VBS-audio-client.patch
Patch0301: 0301-ASoC-Intel-Skl-Virt-Fix-NULL-ptr-in-pcm_close-on-SOS.patch
Patch0302: 0302-ASoC-Intel-Skl-Virt-Fix-logic-of-vbe_skl_pcm_close_a.patch
Patch0303: 0303-ASoC-Intel-Skl-Virt-Cleanup-Klocwork-issues.patch
Patch0304: 0304-ASoC-Intel-Skylake-Enable-codec-command-I-O-function.patch
Patch0305: 0305-ASoC-Intel-Skl-Virt-Check-NULL-ptr-on-virual-FE-atta.patch
Patch0306: 0306-ASoC-dapm-expose-snd_soc_dapm_new_control_unlocked-p.patch
Patch0307: 0307-AsOC-Intel-fix-use-of-potentially-uninitialized-vari.patch
Patch0308: 0308-ASoC-Intel-Skylake-Fix-for-hardcoded-number-of-dmact.patch
Patch0309: 0309-ASoC-Intel-Skylake-use-correct-function-to-access-io.patch
Patch0310: 0310-ASoC-Intel-Skylake-Fix-disabling-interrupts.patch
Patch0311: 0311-ASoC-Intel-Skylake-Add-missing-headers-after-5.1-reb.patch
Patch0312: 0312-ASoC-Intel-Skylake-Fix-build-error.patch
#END XXXX: PK Series

# Clear Linux patch
Patch9001: 9001-init-wait-for-partition-and-retry-scan.patch
Patch9002: 9002-Add-boot-option-to-allow-unsigned-modules.patch
%description
The Linux kernel.

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel

%description extra
Linux kernel extra files

%prep
%setup -q -n linux-5.1

#patchXXXX PK Series
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1
%patch0029 -p1
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1
%patch0034 -p1
%patch0035 -p1
%patch0036 -p1
%patch0037 -p1
%patch0038 -p1
%patch0039 -p1
%patch0040 -p1
%patch0041 -p1
%patch0042 -p1
%patch0043 -p1
%patch0044 -p1
%patch0045 -p1
%patch0046 -p1
%patch0047 -p1
%patch0048 -p1
%patch0049 -p1
%patch0050 -p1
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1
%patch0059 -p1
%patch0060 -p1
%patch0061 -p1
%patch0062 -p1
%patch0063 -p1
%patch0064 -p1
%patch0065 -p1
%patch0066 -p1
%patch0067 -p1
%patch0068 -p1
%patch0069 -p1
%patch0070 -p1
%patch0071 -p1
%patch0072 -p1
%patch0073 -p1
%patch0074 -p1
%patch0075 -p1
%patch0076 -p1
%patch0077 -p1
%patch0078 -p1
%patch0079 -p1
%patch0080 -p1
%patch0081 -p1
%patch0082 -p1
%patch0083 -p1
%patch0084 -p1
%patch0085 -p1
%patch0086 -p1
%patch0087 -p1
%patch0088 -p1
%patch0089 -p1
%patch0090 -p1
%patch0091 -p1
%patch0092 -p1
%patch0093 -p1
%patch0094 -p1
%patch0095 -p1
%patch0096 -p1
%patch0097 -p1
%patch0098 -p1
%patch0099 -p1
%patch0100 -p1
%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0109 -p1
%patch0110 -p1
%patch0111 -p1
%patch0112 -p1
%patch0113 -p1
%patch0114 -p1
%patch0115 -p1
%patch0116 -p1
%patch0117 -p1
%patch0118 -p1
%patch0119 -p1
%patch0120 -p1
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1
%patch0127 -p1
%patch0128 -p1
%patch0129 -p1
%patch0130 -p1
%patch0131 -p1
%patch0132 -p1
%patch0133 -p1
%patch0134 -p1
%patch0135 -p1
%patch0136 -p1
%patch0137 -p1
%patch0138 -p1
%patch0139 -p1
%patch0140 -p1
%patch0141 -p1
%patch0142 -p1
%patch0143 -p1
%patch0144 -p1
%patch0145 -p1
%patch0146 -p1
%patch0147 -p1
%patch0148 -p1
%patch0149 -p1
%patch0150 -p1
%patch0151 -p1
%patch0152 -p1
%patch0153 -p1
%patch0154 -p1
%patch0155 -p1
%patch0156 -p1
%patch0157 -p1
%patch0158 -p1
%patch0159 -p1
%patch0160 -p1
%patch0161 -p1
%patch0162 -p1
%patch0163 -p1
%patch0164 -p1
%patch0165 -p1
%patch0166 -p1
%patch0167 -p1
%patch0168 -p1
%patch0169 -p1
%patch0170 -p1
%patch0171 -p1
%patch0172 -p1
%patch0173 -p1
%patch0174 -p1
%patch0175 -p1
%patch0176 -p1
%patch0177 -p1
%patch0178 -p1
%patch0179 -p1
%patch0180 -p1
%patch0181 -p1
%patch0182 -p1
%patch0183 -p1
%patch0184 -p1
%patch0185 -p1
%patch0186 -p1
%patch0187 -p1
%patch0188 -p1
%patch0189 -p1
%patch0190 -p1
%patch0191 -p1
%patch0192 -p1
%patch0193 -p1
%patch0194 -p1
%patch0195 -p1
%patch0196 -p1
%patch0197 -p1
%patch0198 -p1
%patch0199 -p1
%patch0200 -p1
%patch0201 -p1
%patch0202 -p1
%patch0203 -p1
%patch0204 -p1
%patch0205 -p1
%patch0206 -p1
%patch0207 -p1
%patch0208 -p1
%patch0209 -p1
%patch0210 -p1
%patch0211 -p1
%patch0212 -p1
%patch0213 -p1
%patch0214 -p1
%patch0215 -p1
%patch0216 -p1
%patch0217 -p1
%patch0218 -p1
%patch0219 -p1
%patch0220 -p1
%patch0221 -p1
%patch0222 -p1
%patch0223 -p1
%patch0224 -p1
%patch0225 -p1
%patch0226 -p1
%patch0227 -p1
%patch0228 -p1
%patch0229 -p1
%patch0230 -p1
%patch0231 -p1
%patch0232 -p1
%patch0233 -p1
%patch0234 -p1
%patch0235 -p1
%patch0236 -p1
%patch0237 -p1
%patch0238 -p1
%patch0239 -p1
%patch0240 -p1
%patch0241 -p1
%patch0242 -p1
%patch0243 -p1
%patch0244 -p1
%patch0245 -p1
%patch0246 -p1
%patch0247 -p1
%patch0248 -p1
%patch0249 -p1
%patch0250 -p1
%patch0251 -p1
%patch0252 -p1
%patch0253 -p1
%patch0254 -p1
%patch0255 -p1
%patch0256 -p1
%patch0257 -p1
%patch0258 -p1
%patch0259 -p1
%patch0260 -p1
%patch0261 -p1
%patch0262 -p1
%patch0263 -p1
%patch0264 -p1
%patch0265 -p1
%patch0266 -p1
%patch0267 -p1
%patch0268 -p1
%patch0269 -p1
%patch0270 -p1
%patch0271 -p1
%patch0272 -p1
%patch0273 -p1
%patch0274 -p1
%patch0275 -p1
%patch0276 -p1
%patch0277 -p1
%patch0278 -p1
%patch0279 -p1
%patch0280 -p1
%patch0281 -p1
%patch0282 -p1
%patch0283 -p1
%patch0284 -p1
%patch0285 -p1
%patch0286 -p1
%patch0287 -p1
%patch0288 -p1
%patch0289 -p1
%patch0290 -p1
%patch0291 -p1
%patch0292 -p1
%patch0293 -p1
%patch0294 -p1
%patch0295 -p1
%patch0296 -p1
%patch0297 -p1
%patch0298 -p1
%patch0299 -p1
%patch0300 -p1
%patch0301 -p1
%patch0302 -p1
%patch0303 -p1
%patch0304 -p1
%patch0305 -p1
%patch0306 -p1
%patch0307 -p1
%patch0308 -p1
%patch0309 -p1
%patch0310 -p1
%patch0311 -p1
%patch0312 -p1
# End XXXX PK Series

# Clear Linux patch
%patch9001 -p1
%patch9002 -p1

cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp -a /usr/lib/firmware/i915 firmware/
cp -a /usr/lib/firmware/intel-ucode firmware/
cp -a /usr/lib/firmware/intel firmware/

%build
BuildKernel() {

    Target=$1
    Arch=x86_64
    ExtraVer="-%{release}.${Target}"
#    ExtraVer="_rc4-%{release}.${Target}"
    Config=config

    rm -f localversion-rt

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile
#    perl -p -i -e "s/^(EXTRAVERSION.*)/\$1${ExtraVer}/" Makefile
    perl -p -i -e "s/^CONFIG_LOCALVERSION=.*/CONFIG_LOCALVERSION=\"\"/" ${Config}

    make O=${Target} -s mrproper
    cp ${Config} ${Target}/.config

    make O=${Target} -s ARCH=${Arch} olddefconfig
    make O=${Target} -s ARCH=${Arch} CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} %{?sparse_mflags}
}

BuildKernel %{ktarget0}

%install

InstallKernel() {

    Target=$1
    Kversion=$2
    Arch=x86_64
    KernelDir=%{buildroot}/usr/lib/kernel
#    CmdLine=cmdline
    CmdLine=cmdline-iot-lts2019
    DevDir=%{buildroot}/usr/lib/modules/${Kversion}/build
    KerDir=%{buildroot}/usr/lib/modules/${Kversion}/kernel
    ModDir=%{buildroot}/usr/lib/modules/${Kversion}/modules.

    mkdir   -p ${KernelDir}
    mkdir   -p ${KerDir}
    install -m 644 ${Target}/.config    ${KernelDir}/config-${Kversion}
    install -m 644 ${Target}/System.map ${KernelDir}/System.map-${Kversion}
    install -m 644 ${Target}/vmlinux    ${KernelDir}/vmlinux-${Kversion}
    install -m 644 ${CmdLine}           ${KernelDir}/cmdline-${Kversion}
    cp  ${Target}/arch/x86/boot/bzImage ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules
    mkdir -p ${ModDir}
    make O=${Target} -s ARCH=${Arch} INSTALL_MOD_PATH=%{buildroot}/usr modules_install

    rm -f %{buildroot}/usr/lib/modules/${Kversion}/build
    rm -f %{buildroot}/usr/lib/modules/${Kversion}/source

    mkdir -p ${DevDir}
   # find . -type f -a '(' -name 'Makefile*' -o -name 'Kbuild*' -o -name 'Kconfig*' ')' -exec cp -t ${DevDir} --parents -pr {} +
   # find . -type f -a '(' -name '*.sh' -o -name '*.pl' ')' -exec cp -t ${DevDir} --parents -pr {} +
   # cp -t ${DevDir} -pr ${Target}/{Module.symvers,tools}
   # ln -s ../../../kernel/config-${Kversion} ${DevDir}/.config
   # ln -s ../../../kernel/System.map-${Kversion} ${DevDir}/System.map
   # cp -t ${DevDir} --parents -pr arch/x86/include
   # cp -t ${DevDir}/arch/x86/include -pr ${Target}/arch/x86/include/*
   # cp -t ${DevDir}/include -pr include/*
   # cp -t ${DevDir}/include -pr ${Target}/include/*
   # cp -t ${DevDir} --parents -pr scripts/*
   # cp -t ${DevDir}/scripts -pr ${Target}/scripts/*
   # find  ${DevDir}/scripts -type f -name '*.[cho]' -exec rm -v {} +
   # find  ${DevDir} -type f -name '*.cmd' -exec rm -v {} +
    # Cleanup any dangling links
   # find ${DevDir} -type l -follow -exec rm -v {} + 

    ln -s org.clearlinux.${Target}.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-${Target}
}

InstallKernel %{ktarget0} %{kversion0}

rm -rf %{buildroot}/usr/lib/firmware

%files
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion0}
/usr/lib/kernel/config-%{kversion0}
/usr/lib/kernel/cmdline-%{kversion0}
/usr/lib/kernel/org.clearlinux.%{ktarget0}.%{version}-%{release}
/usr/lib/kernel/default-%{ktarget0}
/usr/lib/modules/%{kversion0}/kernel
/usr/lib/modules/%{kversion0}/modules.*

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/System.map-%{kversion0}
/usr/lib/kernel/vmlinux-%{kversion0}
