'use strict';

document.addEventListener('DOMContentLoaded', function () {

  // ── Máscara CPF ──────────────────────────────────────────
  const cpfInput = document.querySelector('input[name="cpf"]');
  if (cpfInput) {
    cpfInput.addEventListener('input', function () {
      let v = this.value.replace(/\D/g, '').substring(0, 11);
      v = v.replace(/^(\d{3})(\d)/, '$1.$2');
      v = v.replace(/^(\d{3})\.(\d{3})(\d)/, '$1.$2.$3');
      v = v.replace(/\.(\d{3})(\d)/, '.$1-$2');
      this.value = v;
    });
  }

  // ── Máscara CNPJ ─────────────────────────────────────────
  const cnpjInput = document.querySelector('input[name="cnpj"]');
  if (cnpjInput) {
    cnpjInput.addEventListener('input', function () {
      let v = this.value.replace(/\D/g, '').substring(0, 14);
      v = v.replace(/^(\d{2})(\d)/, '$1.$2');
      v = v.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
      v = v.replace(/\.(\d{3})(\d)/, '.$1/$2');
      v = v.replace(/(\d{4})(\d)/, '$1-$2');
      this.value = v;
    });
  }

  // ── Máscara de telefone ───────────────────────────────────
  document.querySelectorAll('input[name*="numero"]').forEach(function (el) {
    el.addEventListener('input', function () {
      let v = this.value.replace(/\D/g, '').substring(0, 11);
      if (v.length <= 10) {
        v = v.replace(/^(\d{2})(\d{4})(\d{0,4})/, '($1) $2-$3');
      } else {
        v = v.replace(/^(\d{2})(\d{5})(\d{0,4})/, '($1) $2-$3');
      }
      this.value = v.trim().replace(/-$/, '');
    });
  });

  // ── Preview da foto ───────────────────────────────────────
  const fotoInput = document.querySelector('input[name="foto"]');
  if (fotoInput) {
    fotoInput.addEventListener('change', function () {
      const file = this.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function (e) {
        let preview = document.getElementById('fotoPreview');
        if (!preview) {
          preview = document.createElement('img');
          preview.id = 'fotoPreview';
          preview.className = 'rounded-circle mt-2';
          preview.style.cssText = 'width:80px;height:80px;object-fit:cover;display:block';
          fotoInput.parentNode.insertBefore(preview, fotoInput.nextSibling);
        }
        preview.src = e.target.result;
      };
      reader.readAsDataURL(file);
    });
  }

  // ── Auto-dismiss alertas após 5s ─────────────────────────
  setTimeout(function () {
    document.querySelectorAll('.alert.alert-success, .alert.alert-info').forEach(function (el) {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(el);
      bsAlert.close();
    });
  }, 5000);

  // ── Confirmação de ação em botões destrutivos ─────────────
  document.querySelectorAll('[data-confirm]').forEach(function (el) {
    el.addEventListener('click', function (e) {
      if (!confirm(this.dataset.confirm)) e.preventDefault();
    });
  });

  // ── Highlight linha da tabela ao clicar ──────────────────
  document.querySelectorAll('.table tbody tr[data-href]').forEach(function (row) {
    row.style.cursor = 'pointer';
    row.addEventListener('click', function () {
      window.location.href = this.dataset.href;
    });
  });

});
