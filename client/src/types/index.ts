export type Option<T> = {
  value: T
  label: string
}

export type Product = {
  id: string
  supplier: Supplier
  created_at: string
  name: string
  price: number
  description: string
  product_code: string
}

export type Supplier = {
  id: string
  name: string
  email: string
  phone: string
  contact_person: string
  notes: string
}
