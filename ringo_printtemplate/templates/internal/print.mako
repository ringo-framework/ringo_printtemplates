<form action="${ok_url}" method="POST" no-dirtyable="true">
  <div class="dialog modal fade" id="myModal">
    <div class="modal-dialog">
      <div class="panel panel-default">
        <div class="panel-heading"><strong>${_('{} for').format(header)} ${modul}</strong></div>
          <div class="panel-body">
            <p>${_("Please select a item from the list below which you want to use for printing. The item will be downloaded and can be opened with an appropriate application.")}</p>
            <p>${body}</p>
            <p>${_("Please click on \"Close\" after you finish printing to close this dialog.")}</p>
          </div>
          <div class="panel-footer">
            <button type"submit" class="btn btn-primary
              nospinner">${_("Download {}").format(ok_text)}</button>
            <a class="btn btn-default" href="${cancel_url}">${_('Close')}</a>
            <input type="hidden" name="confirmed" value="1"/>
            <input type="hidden" name="csrf_token" value="${request.session.get_csrf_token()}"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</form>
