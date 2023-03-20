# helm-learning
## Run docker file within Minikube

If the docker was build locally, not docker hub nor inside minikube, then the image won’t be found. To build the docker image within Minikube, please see below

- `eval $(minikube docker-env)`
- `docker build -t helloworld .`
- Set `imagePullPolicy` to `Never` so that it will only pull the image from the local (here is minikube)
- Refer: [https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube](https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube)

---

## Update docker image in helm

- To find out the local docker image repository: `docker image ls`, select the right image and update it in  `values.yaml` image.
- helm install `helm install hi ./hello-world --dry-run --debug`

---

## Configmap

- Check the configuration: `helm get manifest full-coral`
    - The `helm get manifest` command takes a release name (`full-coral`) and prints out all of the Kubernetes resources that were uploaded to the server
- Create a configmap based on a single file: `kubectl create configmap hello-world --from-file=./app/main.py`
- Get info for the configmap: `kubectl describe configmaps hello-world`

---

## Troubleshooting

- when run `helm install full-coral ./kj-helm`
    - Received an error: `Error: INSTALLATION FAILED: cannot re-use a name that is still in use`
        - use helm upgrade instead, since you can’t install the same thing twice: `KJ-helm helm upgrade full-coral ./kj-helm`
            
            `full-coral` is the release name, it can be anything
            
- display the configmap `kubectl describe configmaps`
- `Error: INSTALLATION FAILED: template: hello-world/templates/serviceaccount.yaml:1:14: executing "hello-world/templates/serviceaccount.yaml" at <.Values.serviceAccount.create>: nil pointer evaluating interface {}.create`
    - set `serviceAccount` into false in `values.yaml`
