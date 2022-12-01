function getBaseURL() {
  const { portalProps } = window.globals;
  const { origin, basePath } = portalProps.backend.api;

  return `${origin ? origin : ''}${basePath ? basePath : ''}`;
}

function request(path) {
  const { portalProps } = window.globals;
  const { token_type: tokenType, access_token: accessToken } =
    portalProps.client.tokenInfo;
  const baseURL = getBaseURL();
  const headers = {
    Authorization: `${tokenType} ${accessToken}`,
  };
  const url = `${baseURL}${path}`;

  return fetch(url, { headers }).then((value) => value.json());
}

((global) => {
  global.lifecycle = {
    bootstrap: (props) => {
      console.log('bootstrap', props);
      return Promise.resolve();
    },
    mount: (props) => {
      console.log('mount', props);
      window.globals = props;
      return render();
    },
    unmount: (props) => {
      console.log('unmount', props);
      return Promise.resolve();
    },
  };
})(window);

function render() {
  handleSubmit();
  return Promise.resolve();
}

function handleSubmit() {
  const formElement = document.getElementById('calc-form');
  const xElement = document.getElementById('x');
  const yElement = document.getElementById('y');

  formElement.addEventListener('submit', (event) => {
    event.preventDefault();
    const x = xElement.value;
    const y = yElement.value;
    const params = { x, y };
    fetchCalc(params).then(handleCalcRes);
  });
}

function fetchCalc(params) {
  const { x, y } = params;
  const url = `/tkeel-calc/calc?x=${x}&y=${y}`;
  return request(url).then((result) => {
    const { code, data } = result;
    if (code === 'io.tkeel.SUCCESS') {
      const res = data.res ?? 20;
      return Promise.resolve(res);
    } else {
      return Promise.reject(result);
    }
  });
}

function handleCalcRes(res) {
  const calcFormResultElement = document.getElementById('calc-form-result');
  calcFormResultElement.innerText = res;
}
